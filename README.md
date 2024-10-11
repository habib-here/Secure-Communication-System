# Secure Communication System

This project implements a **secure communication system** using **AES encryption**, **Diffie-Hellman key exchange**, and a **client-server architecture**. It ensures confidentiality, integrity, and security of messages exchanged between a client and a server. The project also includes user authentication based on hashed and salted passwords.

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Project Structure](#project-structure)
- [Detailed Functionality](#detailed-functionality)
  - [AES Encryption (`AES.py`)](#aes-encryption)
  - [Client-Side (`client.py`)](#client-side)
  - [Server-Side (`server.py`)](#server-side)
- [Usage](#usage)
- [Installation](#installation)
  - [Step 1: Python and Dependencies](#step-1-python-and-dependencies)
  - [Step 2: Running the Server](#step-2-running-the-server)
  - [Step 3: Running the Client](#step-3-running-the-client)
- [Diffie-Hellman Key Exchange](#diffie-hellman-key-exchange)
- [Advanced Encryption Standard (AES)](#advanced-encryption-standard-aes)
- [Authentication Mechanism](#authentication-mechanism)
- [Data Flow](#data-flow)
- [Security Considerations](#security-considerations)
- [Example Scenarios](#example-scenarios)
- [Common Errors](#common-errors)
- [Limitations](#limitations)
- [How It Works](#how-it-works)
  - [Step-by-Step Message Flow](#step-by-step-message-flow)
  - [Example Run](#example-run)
  - [Client Authentication](#client-authentication)
  - [Secure Message Exchange](#secure-message-exchange)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

In today's world, ensuring that data shared over a network is secure is critical. This project demonstrates a **secure communication system** where a client and server can exchange sensitive information in a protected manner using:

- **AES Encryption**: Encrypts the data using AES (Advanced Encryption Standard) in CBC mode for confidentiality.
- **Diffie-Hellman Key Exchange**: Generates a shared secret key between the client and server for secure communication.
- **Client-Server Architecture**: Allows for bi-directional communication between a client and a server.
- **User Authentication**: Verifies users before they can send or receive encrypted messages.

This system is ideal for securely transmitting data across an unsecured network such as the internet, ensuring only authorized users can access the information.

---

## Key Features

### 1. **AES Encryption**:
This project uses **AES encryption (Advanced Encryption Standard)**, one of the most widely used methods for securing data today. Specifically, AES in CBC mode (Cipher Block Chaining) is implemented to ensure data confidentiality.

### 2. **Diffie-Hellman Key Exchange**:
The project leverages the **Diffie-Hellman Key Exchange protocol** to allow the client and server to securely agree on a shared secret key, which is then used for encryption and decryption.

### 3. **Client-Server Architecture**:
This project follows a **client-server architecture** where:
- The server listens for client connections.
- The client connects to the server to exchange encrypted messages.
The communication is handled through Python's socket library.

### 4. **User Authentication**:
The system includes a user authentication process. Before exchanging any data, users are authenticated using a hashed and salted password stored in the system.

---

## Project Structure

The project consists of three main files, each serving a specific role:


### **File Descriptions**:

- **AES.py**: Contains the implementation of AES encryption and decryption functions.
- **client.py**: Represents the client-side of the secure communication system. The client establishes a connection with the server, performs a Diffie-Hellman key exchange, encrypts the message, and sends it to the server.
- **server.py**: Represents the server-side of the secure communication system. The server listens for client connections, completes the Diffie-Hellman key exchange, and decrypts the received messages.

---

## Detailed Functionality

This section describes the detailed functionality of each component in the system.

### AES Encryption

The file `AES.py` provides the core AES encryption and decryption functionality. It handles the generation of the encryption key, encryption of the message using the CBC (Cipher Block Chaining) mode, and decryption of the encrypted message.

#### Key Functions:
- **Key Setup (`setter`)**: Prepares the key used in AES encryption. If the key is less than 16 bytes, it pads the key; if the key is longer, it truncates it to 16 bytes.
  
- **Encryption (`encrypt`)**:
  - Takes plaintext and key as input.
  - Pads the plaintext to match the AES block size.
  - Encrypts the message using AES in CBC mode and returns the ciphertext and initialization vector (IV).

- **Decryption (`decrypt`)**:
  - Takes the ciphertext, key, and IV as input.
  - Decrypts the ciphertext using AES in CBC mode and returns the plaintext.

#### AES Example:
```python
cipher_text, iv = encrypt("My secret data", "mysecretkey")
plain_text = decrypt(cipher_text, "mysecretkey", iv)
