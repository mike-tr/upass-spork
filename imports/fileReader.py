from cryptography.fernet import Fernet
import imports.CONSTS as CONSTS
import imports.keys as keys
import traceback

class efile:
    def __init__(self, pathName, key):
        self.path = pathName
        self.key = key
        self.fkey = Fernet(key)
        self.file = getFile(pathName + CONSTS.SED)
        self.data = self.file.read()
        
        length = self.data.decode();
        if(len(length) > 0):
            self.data = self.fkey.decrypt(self.data);
            self.data = self.data.decode();
        else :
            self.data = "";
        
    def getFilePath(self):
        return self.path + CONSTS.SED;
    
    def save(self):
        data = (self.data).encode();
        self.file.close();
        with open(self.getFilePath(), "wb") as f:
            f.write(self.fkey.encrypt(data));
        self = efile(self.path, self.key);
        

def getFile(pathName):
    try:
        print(pathName + " loaded!")
        return open(pathName, "r+b")
    except:
        print(pathName + " was created!")
        return open(pathName, "w+b")