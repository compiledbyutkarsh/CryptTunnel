# CryptTunnel 🛡️

CryptTunnel is a professional-grade, multi-threaded VPN-tunneling framework built in Python. It provides a secure, encrypted relay for client-server communication using AES-256 encryption.

## Features
- **End-to-End Encryption:** Secured with `cryptography.fernet` (AES-256).
- **Multi-threaded Architecture:** Efficiently handles multiple concurrent clients.
- **Robust Logging:** Built-in observability for real-time traffic monitoring.
- **Interactive Tunneling:** Dynamic client-side input streaming.

## How to Get Started

### 1. Prerequisites
```bash
pip install cryptography
```

### 2. Running the Tunnel
**Start the Server:**
```bash
python3 server.py
```

**Connect the Client:**
```bash
python3 client.py --host 127.0.0.1 --port 8888
```

## Security Disclaimer
This project is for educational purposes. Always use industry-standard protocols for production environments.
