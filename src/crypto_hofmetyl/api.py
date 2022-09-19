from crypto_hofmetyl.crypto import encrypt
from crypto_hofmetyl.crypto import decrypt
from crypto_hofmetyl.file import map_folder

def encrypt_folder(folder, password):
    map_folder(folder, lambda s: encrypt(s, password))

def decrypt_folder(folder, password):
    map_folder(folder, lambda s: decrypt(s, password))