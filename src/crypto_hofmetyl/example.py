from crypto_hofmetyl import api as api
import os

password = "blah"
api.decrypt_folder(api.encrypt_folder("/home/" + os.getlogin() + "/Documents/Test", password), password)