from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

class CryptoEngine:
    def __init__(self, key):
        self.cipher = Fernet(key)

    def encrypt(self, data: bytes) -> bytes:
        return self.cipher.encrypt(data)

    def decrypt(self, data: bytes) -> bytes:
        return self.cipher.decrypt(data)