from validator_collection import checkers
from sys import exit
import random
import socket
import AES
import csv

def create_socket():
    # create the socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # setup an address
    server_address = ('localhost', 8080)
    sock.connect(server_address)

    return sock

def main():
    print("\n\t>>>>>>>>>> XYZ University Chat Client <<<<<<<<<<\n\n")

    # Create socket and connect to the server
    sock = create_socket()

    # sharing key using diffie
    shared_key = diffie_hellman(sock)
    print(shared_key)

    # Printing for choices
    print("1. LOGIN")
    print("2. REGISTER")

    while True:
        # If wants to register
        message = input("You (Client): ")
        if "REGISTER" in message or message == "2":
            register(sock, shared_key)
            continue

        elif message == "exit":
            print("You disconnected from the chat.")
            exit, iv = AES.encrypt(f"exit", shared_key)
            sock.send(exit)
            status = sock.recv(256).decode('utf-8')
            sock.send(iv)
            break

        # For login
        if login(sock, shared_key) == False:
            continue
        else:
            print("Secure communication with server established :)")
            break

    while message != "exit":
        while True:
            # Get user input and send it to the server
            message = input("You (Client): ")


            # If the client sends "exit", terminate the chat
            if message == "exit":
                print("You disconnected from the chat.")
                break

            # Encrypting using Rot13 for server
            message = Rot13(message)
            if message != "":
                break

        # Send the message to the server
        sock.send(message.encode('utf-8'))

        # receive response from server
        response = sock.recv(256).decode('utf-8')

        # Decrypting Rot13 from server
        response = Rot13(response)
        print("Server:", response)

    # Close the socket after communication
    sock.close()

def diffie_hellman(sock):
    p = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD1  # large prime
    g = 3          # alpha...

    privateKey = random.randint(1, p-2)
    public_key = pow(g, privateKey, p)

    # collecting server key
    server_public = sock.recv(256).decode('utf-8')
    server_public = int(server_public)

    # send my public key
    sock.send(f"{public_key}".encode('utf-8'))

    # computing shared key
    return pow(server_public, privateKey, p)

def Rot13(message):
    encrypted = ""
    for m in message:
        if 'a' <= m <= 'z':
            encrypted += chr((ord(m) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= m <= 'Z':
            encrypted += chr((ord(m) - ord('A') + 13) % 26 + ord('A'))
        elif ':' in m:
	        encrypted += m
        else:
            continue  # Non-alphabetic characters are removed from string
    return encrypted

def register(sock, key):
    while(1):
        # input name
        while(1):
            name = input("Enter Name: ").strip()
            if ' ' in name:
                continue            
            elif name != "":
                break

        # input email
        while(1):
            email = input("Enter email: ")
            if checkers.is_email(email):
                break

        # input password
        while(1):
            password = input("Enter password: ").strip()
            if password != "":
                break
            

        # sending
        register = f"REGISTER\{name}\{email}\{password}"
        register, iv = AES.encrypt(register, key)
        sock.send(register)
        status = sock.recv(256).decode('utf-8')
        sock.send(iv)

        # Waiting for validation
        response = sock.recv(256).decode('utf-8')
        if response == 'True':
            print("User Registered successfully")
            break 
        else:
            print("User name is already taken...") 

def login(sock, key):
    while(1):
        # input name/email
        while True:
            id = input("Enter User ID : ").strip()
            if id != "":
                break

        # input password
        while True:
            password = input("Enter Password: ").strip()
            if password != "":
                break

        # sending
        login = f"LOGIN\{id}\{password}"
        login, iv = AES.encrypt(login, key)
        sock.send(login)
        status = sock.recv(256).decode('utf-8')
        sock.send(iv)

        # Waiting for validation
        response = sock.recv(256).decode('utf-8')
        if response == 'LOGIN_SUCCESSFUL':
            print("User Loged in successfully")
            break 
        else:
            print("Invalid User ID or Password...")         

if __name__ == "__main__":
    main()
