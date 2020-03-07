from cryptography.fernet import Fernet

def load_key(pathName):
    try:
        return open(pathName, "rb").read()
    except:
        return write_key(pathName);

def write_key(pathName):
    key = Fernet.generate_key()
    with open(pathName, "wb") as key_file:
        key_file.write(key)
    return key;

