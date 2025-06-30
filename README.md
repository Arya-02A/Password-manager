# 🔐 Password Manager (Tkinter + JSON)
A simple desktop password manager built using Python, Tkinter, and JSON for data storage.
## ✨ Features
- Generate Secure Passwords - Randomly creates strong passwords with letters, numbers, and symbols.
- Save Login Details - Stores website, email/username, and password securely in a local .json file.
- Search Functionality - Instantly retrieve saved credentials by searching with the website name.
## 🛠️ Technologies Used
- Python 3
- Tkinter (GUI library)
- JSON (for storing data locally)
## 📁 File Structure
.
├── main.py               # Main application file
├── logo.png              # Logo image for the GUI
├── password_file.json    # Stores saved passwords (auto-created)
└── README.txt            # This file
## ⚠️ Notes
- If password_file.json doesn't exist or is empty, it will be created automatically.
- All data is stored locally on your machine — there's no encryption, so use it carefully.
- Modify email_input.insert(...) if you want to change the default email shown in the GUI.

