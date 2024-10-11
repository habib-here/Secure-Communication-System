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

