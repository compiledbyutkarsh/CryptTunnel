import socket
import threading
import logging
from utils import CryptoEngine

# Professional Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[logging.StreamHandler()]
)

# KEY: In production, load this from an environment variable or secure .key file
# Use: fernet_key = Fernet.generate_key() to generate a valid key
KEY = b'P4k2nxuWp0pbRINIz_Z5i3xgXRYCfJEMCXaaNusYjgo=' 
crypto = CryptoEngine(KEY)

def handle_client(client_socket, addr):
    """Handles incoming client traffic in a separate thread."""
    logging.info(f"Connection established with {addr}")
    try:
        while True:
            # Receive encrypted data from the tunnel
            encrypted_data = client_socket.recv(4096)
            if not encrypted_data:
                break
            
            # Decrypt the payload
            decrypted_data = crypto.decrypt(encrypted_data)
            logging.info(f"Received from {addr}: {decrypted_data.decode('utf-8')}")
            
    except Exception as e:
        logging.error(f"Communication error with {addr}: {e}")
    finally:
        client_socket.close()
        logging.info(f"Connection closed for {addr}")

def start_server(host='0.0.0.0', port=8888):
    """Initializes the VPN Relay Server."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
    server.listen(10)
    
    logging.info(f"CryptTunnel Server active on {host}:{port}")
    
    try:
        while True:
            client, addr = server.accept()
            # Spawn a new thread for each client to ensure non-blocking relay
            client_thread = threading.Thread(target=handle_client, args=(client, addr))
            client_thread.daemon = True
            client_thread.start()
    except KeyboardInterrupt:
        logging.info("Server shutting down...")
    finally:
        server.close()

if __name__ == "__main__":
    start_server()