from Crypto.Cipher import AES
import hashlib

def get_cipher(password):
    key = hashlib.sha256(password.encode()).digest()
    return AES.new(key, AES.MODE_CFB, key[0:16])

def encrypt(bytes, password):
    return get_cipher(password).encrypt(bytes)

def decrypt(string, password):
    return get_cipher(password).decrypt(string)