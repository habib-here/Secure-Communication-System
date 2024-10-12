
# Secure Communication System

This project implements a secure communication system using cryptographic methods and a client-server architecture. The system ensures data confidentiality and authentication through encryption and secure key exchange protocols.

## Features
- **AES Encryption (CBC/ECB Modes)**: Data is encrypted using the AES (Advanced Encryption Standard) cipher, providing secure transmission of messages between the client and server.
- **Diffie-Hellman Key Exchange**: A method to securely exchange cryptographic keys over a public channel.
- **ROT13 Encryption**: Provides an additional encryption option using the ROT13 cipher.
- **User Authentication**: Verifies client credentials based on hashed passwords and salts.
  
## File Descriptions

### 1. `AES.py`
This module provides functions to encrypt and decrypt messages using the AES encryption standard in both **ECB (Electronic Codebook)** and **CBC (Cipher Block Chaining)** modes.

- **Key Management**: The `setter()` and `setKey()` functions handle key formatting to ensure they meet the 16-byte AES requirement.
- **Encryption**: The `encrypt()` and `encrypt_message()` functions use AES to encrypt a given message.
- **Decryption**: The `decrypt()` and `decrypt_message()` functions decrypt AES-encrypted messages back to plaintext.

### 2. `client.py`
This file implements the client-side of the communication system. It sends encrypted messages to the server and receives encrypted responses.

- **Encryption**: Before sending messages, the client encrypts them using the AES module.
- **Key Exchange**: Uses the Diffie-Hellman protocol to securely exchange keys with the server.
- **ROT13 Option**: An additional ROT13 encryption function is available.

### 3. `server.py`
This file implements the server-side of the communication system. It receives encrypted messages from the client, decrypts them, and handles authentication.

- **Client Authentication**: The server authenticates the client by comparing hashed credentials.
- **Diffie-Hellman Key Exchange**: Securely exchanges keys with the client.
- **ROT13 Option**: Supports decrypting messages using ROT13 as an additional option.

## Installation and Usage

### Requirements
- Python 3.x
- `pycryptodome` for AES encryption:
  ```bash
  pip install pycryptodome
  ```

### Running the System

1. Start the server:
   ```bash
   python server.py
   ```

2. Run the client:
   ```bash
   python client.py
   ```

### Example
```python
# Encrypt a message on the client-side
ciphertext, iv = AES.encrypt("Hello, World!", "password123")

# Decrypt the message on the server-side
plaintext = AES.decrypt(ciphertext, "password123", iv)
```

## Security Considerations
- **Key Length**: AES keys must be 16 bytes long. The `setter()` function automatically pads or truncates keys to ensure this requirement is met.
- **Initialization Vector (IV)**: The AES encryption in CBC mode uses an IV to ensure unique ciphertexts, even with the same plaintext and key.

## License
This project is licensed under the MIT License.
