from cryptography.fernet import Fernet

# Generate and save a key (In production, load this from a secure file)
def generate_key():
    return Fernet.generate_key()

class CryptoEngine:
    def __init__(self, key):
        self.cipher = Fernet(key)

    def encrypt(self, data):
        return self.cipher.encrypt(data)

    def decrypt(self, data):
        return self.cipher.decrypt(data)