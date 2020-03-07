import json
import imports.fileReader as reader

class dataBase:
    def __init__(self, path):
        self.file = reader.efile(path);
        if(len(self.file.data) > 0):
            self.json = json.loads(self.file.data)
        else:
            self.json = json.loads("{}")
    
    def save(self):
        self.file.data = json.dumps(self.json)
        self.file.save();