import socket
import logging
import argparse
import sys
from utils import CryptoEngine

# Configure Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

# KEY (Hardcoded but shared across files)
KEY = b'P4k2nxuWp0pbRINIz_Z5i3xgXRYCfJEMCXaaNusYjgo=' 
crypto = CryptoEngine(KEY)

def start_client(target_host, target_port):
    """Initializes the interactive secure tunnel."""
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        logging.info(f"Connecting to CryptTunnel at {target_host}:{target_port}...")
        client.connect((target_host, target_port))
        logging.info("Tunnel Established! Type your message (or 'exit' to quit).")
        
        while True:
            user_input = input(">> ")
            if user_input.lower() == 'exit':
                break
            
            # Encrypt and send
            encrypted_payload = crypto.encrypt(user_input.encode('utf-8'))
            client.sendall(encrypted_payload)
            
    except ConnectionRefusedError:
        logging.error("Server is offline. Start 'server.py' first.")
    except KeyboardInterrupt:
        logging.info("\nTunnel disconnected by user.")
    except Exception as e:
        logging.error(f"Error: {e}")
    finally:
        client.close()
        logging.info("Tunnel closed.")

if __name__ == "__main__":
    # Command line arguments for flexibility
    parser = argparse.ArgumentParser(description="CryptTunnel Client")
    parser.add_argument("--host", default="127.0.0.1", help="Server IP")
    parser.add_argument("--port", type=int, default=8888, help="Server Port")
    args = parser.parse_args()
    
    start_client(args.host, args.port)