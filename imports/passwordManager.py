import imports.dataHandler as jdata
import imports.passwordToKey as keys
import imports.randomText as rand_text
import pyperclip as clipboard

from cryptography.fernet import Fernet
import json

class passwordManager:
    def __init__(self, pathDir):
        value = input("Enter username : ")
        password = input("Enter password :" ) 
        key = keys.passwordToKey(value, password)
        try:
            self.pathName = pathDir + value
            self.data = jdata.dataBase(pathDir + value, key);
            self.loadFile()
            print(self.data.json)
            # Do something with the file
        except IOError:
            print("Wrong username or password, try again!")
        
        self.data.save();
        self.run();
    
    def run(self):
        run = True;
        while(run):
            value = input("Enter command : ").split();
            if(value[0] == "quit"):
                run = False;
            elif(value[0] == "add"):
                if(len(value) > 2):
                    if(value[2] == "-r" or value[2] == "random"):
                        value[2] = rand_text.randomStringDigits(12);
                    key = Fernet.generate_key();
                    self.data.json[value[1]] = key.decode();
                    jdata = json.loads("{}");
                    jdata["name"] = value[1]
                    jdata["pass"] = value[2]
                    jdata = json.dumps(jdata);
                    fkey = Fernet(key);

                    jdata = fkey.encrypt(jdata.encode())
                    self.kdata.json[value[1]] = jdata.decode();
                    clipboard.copy(value[2]);
                    self.kdata.save();
                    self.data.save();
            elif(value[0] == "load"):
                if(len(value) > 1 and value[1] in self.data.json):
                    key = self.data.json[value[1]].encode();
                    data = self.kdata.json[value[1]];
                    fkey = Fernet(key);
                    data = fkey.decrypt(data.encode())
                    data = json.loads(data.decode());
                    print(data["pass"])
                    print(clipboard.paste())
                    clipboard.copy(data["pass"])


    def loadFile(self):
        if("state" not in self.data.json):
            self.init()
        else:
            key = self.data.json["key"].encode();
            self.kdata = jdata.dataBase(self.pathName + "_data", key)
    
    def init(self):
        self.data.json["state"] = "initialized"
        key = Fernet.generate_key();
        self.data.json["key"] = key.decode();
        self.kdata = jdata.dataBase(self.pathName + "_data", key)
        self.kdata.save();

