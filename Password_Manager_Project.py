import tkinter as tk
from tkinter import messagebox
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

# Sign up a new user
def sign_up():
    email = email_entry.get()
    password = password_entry.get()
    if email and password:
        users = load_users()
        if email in users:
            messagebox.showwarning("Sign Up Error", "Email already exists.")
        else:
            save_user(email, password)
            messagebox.showinfo("Success", "User registered successfully!")
            email_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please fill in both fields.")

# Log in an existing user
def log_in():
    name = name_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if email and password:
        users = load_users()
        if email in users and users[email] == password:
            email_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
            name_entry.delete(0, tk.END)
            show_password_manager(name, email)
        else:
            messagebox.showwarning("Login Error", "Invalid email or password.")
    else:
        messagebox.showwarning("Input Error", "Please fill in both fields.")

# Show all passwords for the logged-in user
def show_passwords(user_email):
    passwords = load_passwords(user_email)
    if passwords:
        passwords_str = "\n".join([f"{service}: {username} - {password}" for service, (username, password) in passwords.items()])
        messagebox.showinfo("Stored Passwords", passwords_str)
    else:
        messagebox.showinfo("Stored Passwords", "No passwords stored.")

# Add a password for a service, including the username
def add_password(service, username, password, user_email):
    if service and username and password:
        save_password(service, username, password, user_email)
        messagebox.showinfo("Success", "Password saved successfully!")
        # Clear the form fields
        service_entry.delete(0, tk.END)
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields.")

# Show the password manager interface after login
def show_password_manager(name, user_email):
    for widget in app.winfo_children():
        widget.destroy()

    tk.Label(app, text=f"Hello {name}!", font=("Helvetica", 16, "bold"), bg="#e6f7ff", fg="#003d99").pack(pady=20)
    tk.Label(app, text="Password Manager", font=("Helvetica", 16, "bold"), bg="#e6f7ff", fg="#003d99").pack(pady=10)

    frame = tk.Frame(app, bg="#cceeff", padx=20, pady=20)
    frame.pack(pady=10)

    global service_entry, username_entry, password_entry

    tk.Label(frame, text="Service:", font=("Helvetica", 12), bg="#cceeff", fg="#003d99").grid(row=0, column=0, pady=10, padx=10)
    service_entry = tk.Entry(frame, font=("Helvetica", 12), width=20)
    service_entry.grid(row=0, column=1, pady=10, padx=10)

    tk.Label(frame, text="Username:", font=("Helvetica", 12), bg="#cceeff", fg="#003d99").grid(row=1, column=0, pady=10, padx=10)
    username_entry = tk.Entry(frame, font=("Helvetica", 12), width=20)
    username_entry.grid(row=1, column=1, pady=10, padx=10)

    tk.Label(frame, text="Password:", font=("Helvetica", 12), bg="#cceeff", fg="#003d99").grid(row=2, column=0, pady=10, padx=10)
    password_entry = tk.Entry(frame, font=("Helvetica", 12), width=20, show="*")
    password_entry.grid(row=2, column=1, pady=10, padx=10)

    tk.Button(frame, text="Add Password", font=("Helvetica", 12), bg="#003d99", fg="white",
              command=lambda: add_password(service_entry.get(), username_entry.get(), password_entry.get(), user_email)).grid(row=3, column=0, pady=10, padx=10)
    tk.Button(frame, text="Show Passwords", font=("Helvetica", 12), bg="#005ce6", fg="white",
              command=lambda: show_passwords(user_email)).grid(row=3, column=1, pady=10, padx=10)

    tk.Button(app, text="Logout", font=("Helvetica", 12), bg="#cc0000", fg="white", width=15, command=logout).pack(pady=20)

# Logout and return to the login screen
def logout():
    for widget in app.winfo_children():
        widget.destroy()
    create_login_screen()

# Create the login screen
def create_login_screen():
    tk.Label(app, text="Secure Password Manager", font=("Helvetica", 16, "bold"), bg="#e6f7ff", fg="#003d99").pack(pady=20)

    form_frame = tk.Frame(app, bg="#cceeff", padx=20, pady=20)
    form_frame.pack(pady=10)

    # Name input
    tk.Label(form_frame, text="Name:", font=("Helvetica", 12), bg="#cceeff", fg="#003d99").grid(row=0, column=0, pady=10, padx=10)
    global name_entry
    name_entry = tk.Entry(form_frame, font=("Helvetica", 12), width=20)
    name_entry.grid(row=0, column=1, pady=10, padx=10)

    # Email input
    tk.Label(form_frame, text="Email:", font=("Helvetica", 12), bg="#cceeff", fg="#003d99").grid(row=1, column=0, pady=10, padx=10)
    global email_entry
    email_entry = tk.Entry(form_frame, font=("Helvetica", 12), width=20)
    email_entry.grid(row=1, column=1, pady=10, padx=10)

    # Password input
    tk.Label(form_frame, text="Password:", font=("Helvetica", 12), bg="#cceeff", fg="#003d99").grid(row=2, column=0, pady=10, padx=10)
    global password_entry
    password_entry = tk.Entry(form_frame, font=("Helvetica", 12), width=20, show="*")
    password_entry.grid(row=2, column=1, pady=10, padx=10)

    button_frame = tk.Frame(app, bg="#e6f7ff")
    button_frame.pack(pady=20)

    tk.Button(button_frame, text="Sign Up", font=("Helvetica", 12), bg="#003d99", fg="white", width=15, command=sign_up).grid(row=0, column=0, padx=10)
    tk.Button(button_frame, text="Log In", font=("Helvetica", 12), bg="#005ce6", fg="white", width=15, command=log_in).grid(row=0, column=1, padx=10)

    tk.Label(app, text="Secure your data with encryption.\n© Sudais Khalid", font=("Helvetica", 10), bg="#e6f7ff", fg="#003d99").pack(pady=20)

# Create the main app window
app = tk.Tk()
app.title("Secure Password Manager")
app.geometry("400x500")
app.configure(bg="#e6f7ff")

create_login_screen()

app.mainloop()
