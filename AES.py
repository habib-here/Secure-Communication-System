from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

'''
# Correctly define key
key = 1234
data = "My data"
'''

def setter(key):
    key = f"{key}"

    if len(key) < 16:
        key += "0" * (16 - len(key))
    elif len(key) > 16:
        key = key[:16]

    key = key.encode()
    return key

def encrypt(data, key):
    data = data.encode('utf-8') 
    key = setter(key)

    # Encrypting the data
    cipher = AES.new(key, AES.MODE_CBC)  # Create a new AES cipher in CBC mode
    cipher_text = cipher.encrypt(pad(data, AES.block_size))  # Pad and encrypt the data
    iv = cipher.iv  # Save the initialization vector
    # print("Cipher text:", cipher_text)
    return cipher_text, iv

def decrypt(cipher_text, key, iv = b"1234567890123456"):
    key = setter(key)
    # Decrypting the data
    decrypt_cipher = AES.new(key, AES.MODE_CBC, iv)  # Create a new AES cipher for decryption
    plain_text = unpad(decrypt_cipher.decrypt(cipher_text), AES.block_size)  # Decrypt and unpad the data
    # print("Decrypted text:", plain_text.decode('utf-8'))  # Decode to get the original string
    return plain_text

'''
cypher, iv = encrypt(data, key)
plain_text = decrypt(cypher, key, iv)
'''
""" from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib

def setKey(key):
    if len(key) < 16:
        key = key + ('0' * 16 - (len(key)))
    elif len(key) > 16:
        key = key[:16]

    return key

def encrypt_message(message, key):

    key = setKey(key)
    # Create an AES cipher object in ECB mode
    cipher = AES.new(key, AES.MODE_ECB)
    
    # Pad the message to be a multiple of 16 bytes (AES block size)
    padded_message = pad(message.encode('utf-8'), AES.block_size)
    
    # Encrypt the padded message
    encrypted_message = cipher.encrypt(padded_message)
    
    return encrypted_message

def decrypt_message(encrypted_message, key):
    key = set_key(key)
    # Create an AES cipher object in ECB mode
    cipher = AES.new(key, AES.MODE_ECB)
    
    # Decrypt the message
    decrypted_padded_message = cipher.decrypt(encrypted_message)
    
    # Unpad the decrypted data to get the original message
    decrypted_message = unpad(decrypted_padded_message, AES.block_size).decode('utf-8')
    
    return decrypted_message
 """