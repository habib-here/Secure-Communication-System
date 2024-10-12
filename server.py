import hashlib
import random
import socket
import AES
import csv
import os

def main():
    print("\n\t>>>>>>>>>> XYZ University Chat Server <<<<<<<<<<\n\n")

    # create the server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # define the server address
    server_address = ('', 8080)

    # bind the socket to the specified IP and port
    server_socket.bind(server_address)
    server_socket.listen(5)

    while True:
        # accept incoming connections
        client_socket, client_address = server_socket.accept()

        # create a new process to handle the client
        pid = os.fork()
    
        if pid == -1:
            print("Error! Unable to fork process.")
        elif pid == 0:
            # child process handles the client
            handle_client(client_socket)
            os._exit(0)
        else:
            # parent process continues accepting clients
            client_socket.close()
        


def handle_client(client_socket):
    # sharing key using diffie
    shared_key = diffie_hellman(client_socket)
    print(shared_key)

    while True:
        # receive message from the client
        buf = client_socket.recv(256)
        client_socket.send("buf_s".encode('utf-8'))
        iv = client_socket.recv(256)
        buf = AES.decrypt(buf, shared_key, iv).decode('utf-8')

        # register check
        if buf.startswith("REGISTER"):
            data = buf.split("\\")
            #print(*data)
            
            if userExists(data[1]):
                client_socket.send("False".encode('utf-8'))
            else:
                # Salting password
                data[3] += data[1]

                # Hashing password
                data[3] = hashlib.sha256(data[3].encode('utf-8')).hexdigest()

                save(data[1:])
                client_socket.send("True".encode('utf-8'))
            continue

        elif buf.startswith("LOGIN"):
            data = buf.split("\\")
            #print(*data)
            if authentication(data):
                client_socket.send("LOGIN_SUCCESSFUL".encode('utf-8'))
                break
            else:
                client_socket.send("LOGIN_UNSUCCESSFUL".encode('utf-8'))
                continue
        
        elif buf == "exit":
            print("Client disconnected from server successfully :)")
            client_socket.close()
            exit(0)

    while True:
        # waiting for client Response
        buf = client_socket.recv(256).decode('utf-8')

        # Decrypting message from client       
        buf = Rot13(buf)

        # if client sends "exit", close the connection
        if buf == "exit" or buf == "" or buf == "rkvg":
            print("Client disconnected.")
            break

        print("Client:", buf)

        while True:
            # send a response back to the client
            response = input("You (Server): ")

            # Encrypting server message using Rot13
            response = Rot13(response)
            if response != "":
                break
                
        client_socket.send(response.encode('utf-8'))

    client_socket.close()


def save(data_list, filename="creds.txt"):
    with open(filename, 'a') as csvfile:
        csv_writer = csv.writer(csvfile)
        # Write the data list as a single row
        csv_writer.writerow(data_list)
        print(f"Data successfully stored to '{filename}'.")


def retrieve(filename="creds.txt"):
    try:
        with open(filename) as file:
            data = []
            csv_reader = csv.reader(file)

            for row in csv_reader:
                data.append(row)
            
            if not data:
                print("The CSV file is empty or contains only empty lines.")
            
            return (data)

    except FileNotFoundError:
        print("File does not exist")
        return None

def userExists(user):
    data = retrieve()

    if data:
        for row in data:
            if user == row[0]:
                return True
    return False

def authentication(creds):
    # cred = ["LOGIN", {id}, {password} ]
    # row  = [{name}, {email}, {password i.e hash}]
    if data:
        for row in data:
            if row[0] == creds[1] or row[1] == creds[1]:
                # successfully found user
                # now salt recived pass w.r.t user
                temp = creds[2] + row[0]
                temp = hashlib.sha256(temp.encode('utf-8')).hexdigest()
                if row[2] == temp:
                    return True
    return False


def diffie_hellman(client_socket):
    p = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD1  # large prime
    g = 3   # alpha...

    privateKey = random.randint(1, p-2)
    public_key = pow(g, privateKey, p)
    
    # send my public key
    client_socket.send(f"{public_key}".encode('utf-8'))

    # collecting client key
    client_public = client_socket.recv(256).decode('utf-8')
    client_public = int(client_public)

    # computing shared key
    return pow(client_public, privateKey, p)


def Rot13(message):
    encrypted = ""
    for m in message:
        if 'a' <= m <= 'z':
            encrypted += chr((ord(m) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= m <= 'Z':
            encrypted += chr((ord(m) - ord('A') + 13) % 26 + ord('A'))
        elif ':' in m:
            m += encrypted
        else:
            continue  # Non-alphabetic characters are removed from string
    return encrypted


if __name__ == "__main__":
    main()
