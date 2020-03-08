import imports.dataHandler as jdata
import imports.passwordToKey as keys
import imports.randomText as rand_text
import pyperclip as clipboard

from cryptography.fernet import Fernet
from getpass import getpass
import json

class passwordManager:
    def __init__(self, pathDir):
        while(True):
            value = input("Enter username : ")
            print("Enter password")
            password = getpass() 
            key = keys.passwordToKey(value, password)
            try:
                self.pathName = pathDir + value
                self.data = jdata.dataBase(pathDir + value, key);
                self.key = key;
                self.user = value;
                self.loadFile()
                break
                #print(self.data.json)
                # Do something with the file
            except:
                print("Wrong username or password, try again!")
        self.run();
    
    def confirm(self):
        value = input("confirm to procced! y/n : ")
        if(value.lower() == "y" or value.lower() == "yes"):
            print("Enter password to confirm :")
            password = getpass() 
            key = keys.passwordToKey(self.user, password)
            if(key == self.key):
                return True
            print("wrong password try again!")
            return self.confirm()
        return False;


    def run(self):
        run = True;
        while(run):
            value = input("Enter command : ").split();
            if(value[0] == "quit"):
                run = False;
            elif(value[0] == "add"):
                if(len(value) > 2):
                    add = True
                    if(value[1] in self.data.json):
                        print("there already exist a record with the same name!")
                        add = self.confirm()
                    if(add):
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
                        print("copied the password to clipboard!")
                else:
                    print("invalid syntax : valid syntax example")
                    print("add example_name example_password/random/-r")
            elif(value[0] == "load"):
                if(len(value) > 1):
                    if(value[1] in self.data.json):
                        key = self.data.json[value[1]].encode();
                        data = self.kdata.json[value[1]];
                        fkey = Fernet(key);
                        data = fkey.decrypt(data.encode())
                        data = json.loads(data.decode());
                        #print(data["pass"])
                        #print(clipboard.paste())
                        clipboard.copy(data["pass"])
                        print("copied the password to clipboard!")
                    else:
                        print(value[1] ," record doesnt exist!")
                else:
                    print("invalid syntax : valid syntax example")
                    print("load example_name")


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
        self.data.save();

