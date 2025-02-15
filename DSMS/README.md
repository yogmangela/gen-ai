# 🔒 Data Security Management System

## 📌 Overview
This is a **Flask-based Data Security Management System** that helps:
✅ Encrypt & store sensitive data securely  
✅ Classify data as **Public, Confidential (PII), or Restricted (PHI)**  
✅ Prevent **Data Loss** using **DLP (Data Loss Prevention)**  
✅ Enforce **Record Retention Policies**  
✅ Securely delete data **(Overwriting + Purging)**  
✅ Maintain **Audit Logs** for tracking data modifications  

---

## 🚀 Features
✔ **Flask Web Dashboard** for an easy-to-use interface  
✔ **SQLite Database Integration** for secure data storage  
✔ **Logging System** to track sensitive actions  
✔ **Secure Encryption** using `cryptography.fernet`  
✔ **Role-Based Access Control** for better security  

---

## 📂 Folder Structure
📂 data-security-system/
├── setup.sh               # Automated Setup Script
├── app.py                 # Flask Web Application
├── database.py            # Database Initialization & Logging
├── secure_storage.py      # Encryption Key Management
├── encryption.key         # Secure Encryption Key (Auto-Generated)
├── data_security.db       # SQLite Database (Auto-Generated)
├── templates/
│   ├── index.html         # Web UI
└── README.md              # Step-by-Step Guide

---

## 🔧 Prerequisites
Make sure you have the following installed:
- **Python 3** (`python3 --version`)
- **pip3 (Python package manager)** (`pip3 --version`)
- **Homebrew (for MacOS users, if needed)** (`brew install python3`)

---

## 🛠️ Installation & Setup
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/data-security-system.git
cd data-security-system

chmod +x setup.sh

./setup.sh
```