import streamlit as st
from cryptography.fernet import Fernet
import os

# Generate a key for encryption
def generate_key():
    return Fernet.generate_key()

# Load or create a key
def load_key():
    if os.path.exists("key.key"):
        return open("key.key", "rb").read()
    else:
        key = generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
        return key

# Encrypt the password
def encrypt_password(password):
    f = Fernet(load_key())
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password

# Decrypt the password
def decrypt_password(encrypted_password):
    f = Fernet(load_key())
    decrypted_password = f.decrypt(encrypted_password).decode()
    return decrypted_password

# Save user credentials to a text file
def save_user(email, password):
    encrypted_password = encrypt_password(password).decode()
    with open("users.txt", "a") as file:
        file.write(f"{email}:{encrypted_password}\n")

# Load user credentials from the text file
def load_users():
    if os.path.exists("users.txt"):
        with open("users.txt", "r") as file:
            users = {}
            for line in file:
                email, encrypted_password = line.strip().split(":")
                users[email] = decrypt_password(encrypted_password.encode())
            return users
    return {}

# Save password to a user's specific text file
def save_password(service, username, password, user_email):
    encrypted_password = encrypt_password(password).decode()
    user_file = f"{user_email}_passwords.txt"
    with open(user_file, "a") as file:
        file.write(f"{service}:{username}:{encrypted_password}\n")

# Load passwords from the user's specific text file
def load_passwords(user_email):
    user_file = f"{user_email}_passwords.txt"
    if os.path.exists(user_file):
        with open(user_file, "r") as file:
            passwords = {}
            for line in file:
                service, username, encrypted_password = line.strip().split(":")
                passwords[service] = (username, decrypt_password(encrypted_password.encode()))
            return passwords
    return {}

# Main function to run the Streamlit app
def main():
    st.title("Secure Password Manager")
    st.sidebar.title("Navigation")

    # Initialize session state variables
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'user_email' not in st.session_state:
        st.session_state.user_email = None

    # Login/Sign Up Section
    if not st.session_state.logged_in:
        st.write("### Login / Sign Up")
        email = st.text_input("Email", key="email")
        password = st.text_input("Password", type="password", key="password")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Log In"):
                users = load_users()
                if email in users and users[email] == password:
                    st.session_state.logged_in = True
                    st.session_state.user_email = email
                    st.success("Logged in successfully!")
                else:
                    st.error("Invalid email or password.")
        with col2:
            if st.button("Sign Up"):
                if email and password:
                    users = load_users()
                    if email in users:
                        st.error("Email already exists.")
                    else:
                        save_user(email, password)
                        st.success("User registered successfully!")
                else:
                    st.error("Please fill in both fields.")

    # Password Manager Section (Visible after login)
    else:
        st.sidebar.write(f"Logged in as {st.session_state.user_email}")
        if st.sidebar.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.user_email = None
            st.success("Logged out successfully!")

        st.write("### Password Manager")
        service = st.text_input("Service")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Add Password"):
            if service and username and password:
                save_password(service, username, password, st.session_state.user_email)
                st.success("Password saved successfully!")
            else:
                st.error("Please fill in all fields.")

        if st.button("Show Passwords"):
            passwords = load_passwords(st.session_state.user_email)
            if passwords:
                st.write("Stored Passwords:")
                for service, (username, password) in passwords.items():
                    st.write(f"{service}: {username} - {password}")
            else:
                st.info("No passwords stored.")

if __name__ == "__main__":
    main()