import imports.dataHandler as jdata
import imports.passwordToKey as keys
import imports.randomText as rand_text
import pyperclip as clipboard

from cryptography.fernet import Fernet
from getpass import getpass
import json

protected = ["key", "state"]


class passwordManager:
    def __init__(self, pathDir):
        while(True):
            value = input("Enter username : ")
            print("Enter password")
            password = getpass()
            key = keys.passwordToKey(value, password)
            try:
                self.pathName = pathDir + value
                self.data = jdata.dataBase(pathDir + value, key)
                self.key = key
                self.user = value
                self.loadFile()
                break
                # print(self.data.json)
                # Do something with the file
            except:
                print("Wrong username or password, try again!")
        self.run()

    def loadFile(self):
        if("state" not in self.data.json):
            self.confirmPass()
            self.init()
        else:
            key = self.data.json["key"].encode()
            self.kdata = jdata.dataBase(self.pathName + "_data", key)

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
        return False

    def isProtected(self, value, log=True):
        pr = False
        for name in protected:
            if(value == name):
                pr = True
                break
        if(pr and log):
            print("this name is protected, try different name")
        return pr

    def confirmPass(self):
        while(True):
            print("Enter password to confirm :")
            password = getpass()
            key = keys.passwordToKey(self.user, password)
            if(key == self.key):
                return True
            print("wrong password try again!")

    def getHelp(self):
        print("commands : ")
        print("add example_unqiue_name example_username/-n example_password/random/-r")
        print("load unqiue_name or load unique_name -n (copy username then password)")
        print("remove or delete -n")
        print("records : show all records")
        print("help")

    def run(self):
        run = True
        self.getHelp()
        while(run):
            value = input("Enter command : ").split()
            if(value[0] == "quit"):
                run = False
            elif(value[0] == "add"):
                if(len(value) > 3 and not self.isProtected(value[1])):
                    add = True
                    if(value[1] in self.data.json):
                        print(
                            "there already exist a record with the same unique_name!")
                        add = self.confirm()
                    if(add):
                        if(value[3] == "-r" or value[3] == "random"):
                            value[3] = rand_text.randomStringDigits(12)
                        key = Fernet.generate_key()
                        self.data.json[value[1]] = key.decode()
                        jdata = json.loads("{}")
                        jdata["name"] = value[1]
                        if(value[2] == "-n"):
                            jdata["username"] = value[1]
                        else:
                            jdata["username"] = value[2]
                        jdata["pass"] = value[3]
                        jdata = json.dumps(jdata)
                        fkey = Fernet(key)

                        jdata = fkey.encrypt(jdata.encode())
                        self.kdata.json[value[1]] = jdata.decode()
                        clipboard.copy(value[3])
                        self.kdata.save()
                        self.data.save()
                        print("copied the password to clipboard!")
                else:
                    print("invalid syntax : valid syntax example")
                    print(
                        "add example_unqiue_name example_username/-n example_password/random/-r")
            elif(value[0] == "load"):
                if(len(value) > 1 and not self.isProtected(value[1])):
                    if(value[1] in self.data.json):
                        key = self.data.json[value[1]].encode()
                        data = self.kdata.json[value[1]]
                        fkey = Fernet(key)
                        data = fkey.decrypt(data.encode())
                        data = json.loads(data.decode())
                        # print(data["pass"])
                        # print(clipboard.paste())
                        if(len(value) > 2 and value[2] == "-n"):
                            clipboard.copy(data["username"])
                            print("copied username to clipboard!")
                            value = input("copy password y/n : ")
                            if(value.lower() == "y" or value.lower() == "yes"):
                                clipboard.copy(data["pass"])
                                print("copied the password to clipboard!")
                        else:
                            clipboard.copy(data["pass"])
                            print("username : ", data["username"])
                            print("copied the password to clipboard!")

                    else:
                        print(value[1], " record doesnt exist!")
                else:
                    print("invalid syntax : valid syntax example")
                    print(
                        "load unqiue_name or load unique_name -n (copy username then password)")
            elif(value[0] == "clear"):
                import os
                os.system('cls' if os.name == 'nt' else 'clear')
            elif(value[0] == "help"):
                self.getHelp()
            elif(value[0] == "remove" or value[0] == "delete"):
                self.delete(value)
            elif(value[0] == "records"):
                i = 0
                for record in self.data.json:
                    if(not self.isProtected(record, False)):
                        i += 1
                        print("(", i, ") : ", record)

    def delete(self, user_input):
        if(self.isProtected(user_input[1])):
            # a.k.a values we dont want to delete
            return
        if(user_input[1] in self.data.json):
            value = input("you sure you want to delete this record y/n : ")
            if(value.lower() == "y" or value.lower() == "yes"):
                del self.data.json[user_input[1]]
                self.data.save()

    def init(self):
        self.data.json["state"] = "initialized"
        key = Fernet.generate_key()
        self.data.json["key"] = key.decode()
        self.kdata = jdata.dataBase(self.pathName + "_data", key)
        self.kdata.save()
        self.data.save()
