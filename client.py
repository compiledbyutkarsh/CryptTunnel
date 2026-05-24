import socket
from utils import CryptoEngine

KEY = b'your-32-byte-secure-key-here='
crypto = CryptoEngine(KEY)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8888))

message = "Secure Tunnel Data"
encrypted_data = crypto.encrypt(message.encode())
client.send(encrypted_data)

client.close()