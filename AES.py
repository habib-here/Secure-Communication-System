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
