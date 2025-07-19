# Secure Password Manager 🔐

A comprehensive software application designed to address the growing need for secure password storage and management. This project leverages the power of encryption to ensure the confidentiality and integrity of user credentials with a user-friendly interface.

## 📋 Table of Contents
- [Abstract](#abstract)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Implementation Details](#implementation-details)
- [Security Features](#security-features)
- [Project Structure](#project-structure)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Abstract

The Secure Password Manager is a comprehensive software application that leverages the Fernet symmetric encryption algorithm to ensure the confidentiality and integrity of user credentials. Built with Python's Streamlit library, the application provides a user-friendly GUI that allows users to register, log in, and manage passwords for various services efficiently. Each user's data is securely stored in isolated, encrypted files, ensuring maximum privacy and security.

## ✨ Features

- **User Registration & Authentication**: Secure sign-up and login system with email and password
- **Advanced Encryption**: Utilizes Fernet symmetric encryption algorithm for robust password protection
- **Credential Management**: Store and retrieve passwords for different services with associated usernames
- **Data Isolation**: Each user's credentials are stored in separate encrypted files for enhanced privacy
- **Intuitive GUI**: Clean and minimalistic interface built with Streamlit
- **Secure Key Management**: Automatic generation and secure storage of encryption keys
- **Multi-Service Support**: Manage credentials for various platforms (Gmail, Facebook, etc.)

## 🛠️ Technologies Used

- **Programming Language**: Python
- **GUI Framework**: Streamlit
- **Encryption Library**: Cryptography (Fernet)
- **File Management**: OS module for secure file operations

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/muhammadsudaiskhalid/secure-password-manager.git
   cd secure-password-manager
   ```

2. **Install required dependencies**:
   ```bash
   pip install streamlit cryptography
   ```

3. **Run the application**:
   ```bash
   streamlit run app.py
   ```

## 🚀 Usage

### Getting Started

1. **Registration**: 
   - Launch the application
   - Create a new account with your email and a secure password
   - Your credentials will be encrypted and stored securely

2. **Login**:
   - Enter your registered email and password
   - Access your personal password vault

3. **Managing Passwords**:
   - **Add Password**: Store credentials for new services
   - **View Passwords**: Retrieve and decrypt your stored passwords
   - **Service Management**: Organize passwords by service names

### Example Workflow

```python
# Register a new user
Email: user@example.com
Password: SecurePassword123!

# Add a new service credential
Service: Gmail
Username: user@gmail.com  
Password: MyGmailPassword456
```

## 🔧 Implementation Details

### Encryption and Key Management
- Generates unique encryption keys using the Fernet algorithm
- Securely stores keys in `key.key` file
- All passwords are encrypted before storage

### User Authentication
- User credentials stored in encrypted `users.txt` file
- Password verification through secure decryption and matching
- Session management for authenticated users

### Password Storage
- Individual encrypted files for each user (`<user_email>_passwords.txt`)
- Service-based organization of credentials
- Secure encryption/decryption on demand

### GUI Design
- Streamlit-based responsive interface
- Intuitive navigation and user experience
- Clean, minimalistic design philosophy

## 🔒 Security Features

- **Fernet Symmetric Encryption**: Industry-standard encryption algorithm
- **Isolated User Data**: Separate encrypted files for each user
- **Secure Key Storage**: Protected encryption key management
- **Password Hashing**: User passwords are encrypted before storage
- **No Plain Text Storage**: All sensitive data is encrypted at rest

## 📁 Project Structure

```
secure-password-manager/
├── app.py                 # Main application file
├── key.key               # Encryption key (auto-generated)
├── users.txt             # Encrypted user credentials
├── *_passwords.txt       # User-specific encrypted password files
├── requirements.txt      # Project dependencies
└── README.md            # Project documentation
```

## 🚀 Future Enhancements

- [ ] **Two-Factor Authentication (2FA)**: Additional security layer
- [ ] **Password Generator**: Built-in strong password creation tool
- [ ] **Mobile Application**: Cross-platform accessibility
- [ ] **Cloud Backup**: Secure cloud-based synchronization
- [ ] **Password Strength Analyzer**: Real-time password security assessment
- [ ] **Backup/Export Features**: Data portability options
- [ ] **Multi-Factor Authentication**: Enhanced security options

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

**Muhammad Sudais Khalid**
- 📧 Email: [muhammadsudaiskhalid.artificialintelligence@stmu.edu.pk](mailto:muhammadsudaiskhalid.artificialintelligence@stmu.edu.pk)
- 💼 LinkedIn: [https://www.linkedin.com/in/sudais-khalid/](https://www.linkedin.com/in/sudais-khalid/)
- 💬 Discord: [https://discord.com/invite/cfjfrec9](https://discord.com/invite/cfjfrec9)
- 🌐 Project Link: [https://github.com/muhammadsudaiskhalid/secure-password-manager](https://github.com/muhammadsudaiskhalid/secure-password-manager)

---

⭐ **If you found this project helpful, please give it a star!** ⭐

## 🙏 Acknowledgments

- Thanks to **Ma'am Sana Akram** and **Sir Syed Muneel** for their guidance
- Inspiration from modern password management solutions
- Python cryptography community for excellent documentation
- Streamlit team for the amazing GUI framework

---

*This project demonstrates the practical implementation of information security concepts and showcases the importance of encryption in software development.*
