from cryptography.fernet import Fernet
import imports.CONSTS as CONSTS
import imports.keys as keys
import traceback

FLED = ".srq"
FKEY = ".key"

class efile:
    def __init__(self, pathName):
        self.path = pathName;
        self.fkey = keys.load_key(pathName + FKEY)
        self.fkey = Fernet(self.fkey)
        self.file = getFile(pathName + CONSTS.SED)
        self.data = self.file.read()
        
        length = self.data.decode();
        print("new file")
        if(len(length) > 0):
            self.data = self.fkey.decrypt(self.data);
            self.data = self.data.decode();
            print(self.data)
        else :
            self.data = "";
        
    def getFilePath(self):
        return self.path + CONSTS.SED;
    
    def save(self):
        data = (self.data).encode();
        self.file.close();
        with open(self.getFilePath(), "wb") as f:
            f.write(self.fkey.encrypt(data));
        self = efile(self.path);
        

def getFile(pathName):
    try:
        return open(pathName, "r+b")
    except:
        print("rb2")
        return open(pathName, "w+b")