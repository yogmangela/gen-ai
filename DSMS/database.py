import sqlite3

DB_FILE = "data_security.db"

def log_action(action, details):
    """Logs an action into the database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO logs (action, details) VALUES (?, ?)", (action, details))
    conn.commit()
    conn.close()