import json
import imports.fileReader as reader

class dataBase:
    def __init__(self, path, key):
        self.file = reader.efile(path, key);
        if(len(self.file.data) > 0):
            self.json = json.loads(self.file.data)
        else:
            self.json = json.loads("{}")
            self.json["key"] = key.decode()
    
    def save(self):
        self.file.data = json.dumps(self.json)
        self.file.save();