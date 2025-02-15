from cryptography.fernet import Fernet

def load_key():
    """Loads the encryption key from a secure file."""
    with open("encryption.key", "rb") as key_file:
        return key_file.read()

ENCRYPTION_KEY = load_key()
cipher = Fernet(ENCRYPTION_KEY)