import socket
import threading
from utils import CryptoEngine

# Use a secure way to load this key in production
KEY = b'your-32-byte-base64-key-here=' 
crypto = CryptoEngine(KEY)

def handle_client(client_socket, addr):
    print(f"[+] Connection from {addr}")
    try:
        while True:
            data = client_socket.recv(4096)
            if not data: break
            decrypted = crypto.decrypt(data)
            print(f"[>] Data: {decrypted.decode()}")
    except Exception as e:
        print(f"[!] Error: {e}")
    finally:
        client_socket.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8888))
server.listen(5)
print("[*] CryptTunnel Server running on port 8888...")

while True:
    client, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(client, addr))
    thread.daemon = True
    thread.start()