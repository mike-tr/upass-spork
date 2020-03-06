from cryptography.fernet import Fernet
import tools.CONSTS as CONSTS

t = open(CONSTS.LOGIN, "w+")
t2 = open("test.txt", "w+")

def write_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    return key;

def load_key():
    try:
        return open("key.key", "rb").read()
    except:
        return write_key();

key = load_key();
print(key)