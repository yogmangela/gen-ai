#!/bin/bash

echo "🚀 Setting up the Data Security Management System..."

# 1. Update & Install Dependencies
echo "📦 Installing required Python packages..."
pip install flask cryptography sqlite3

# 2. Generate the encryption key
echo "🔑 Generating encryption key..."
python3 -c "
from cryptography.fernet import Fernet;
key = Fernet.generate_key();
with open('encryption.key', 'wb') as f: f.write(key);
print('✅ Encryption key saved securely.')
"

# 3. Set up the SQLite database
echo "📂 Initializing database..."
python3 -c "
import sqlite3;
conn = sqlite3.connect('data_security.db');
cursor = conn.cursor();
cursor.execute('''
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    action TEXT,
    details TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''');
cursor.execute('''
CREATE TABLE IF NOT EXISTS records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data TEXT,
    classification TEXT,
    encrypted_data TEXT
)
''');
conn.commit();
conn.close();
print('✅ Database initialized successfully.')
"

# 4. Run the Flask app
echo "🚀 Starting the Flask Web Application..."
python3 app.py