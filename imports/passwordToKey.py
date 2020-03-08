from hashlib import scrypt
from os import urandom
from base64 import urlsafe_b64encode

def passwordToKey(userName ,password):
    salt = urandom(16)
    key = scrypt(password.encode(), salt=userName.encode(), n=16384, r=8, p=1, dklen=32)
    return urlsafe_b64encode(key)