import socket
import threading
from utils import CryptoEngine

KEY = b'your-32-byte-secure-key-here=' # Use generate_key() to get this
crypto = CryptoEngine(KEY)

def handle_client(client_socket):
    try:
        while True:
            data = client_socket.recv(4096)
            if not data: break
            decrypted_data = crypto.decrypt(data)
            print(f"[+] Received: {decrypted_data.decode()}")
    except Exception as e:
        print(f"[-] Error: {e}")
    finally:
        client_socket.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8888))
server.listen(5)
print("[*] CryptTunnel Server Active...")

while True:
    client, addr = server.accept()
    threading.Thread(target=handle_client, args=(client,)).start()