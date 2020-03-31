import threading
from time import sleep
from pynput import keyboard

class inputHandler(threading.Thread):
    def __init__(self, id, selfUpdate, updateTime = 0.2):
        threading.Thread.__init__(self)
        self.down = {};
        self.pressed = {};
        self.realesed = {};
        self.id = id
        self.running = True
        if(selfUpdate):
            self.runUpdate(updateTime)
    def runUpdate(self, time):
        t = threading.Thread(target = self.update, args = (10,))
        t.start();

    def update(self, tt):
        while(self.running):
            for key in list(self.pressed):
                print(key)
            sleep(0.1);
            self.updateKeys()

    def run(self):
        with keyboard.Listener(
        on_press=self.on_press,
        on_release=self.on_release) as listener:
            listener.join()
    
    def on_press(self, key):
        if(format(key) not in self.pressed):
            if(format(key) not in self.down):
                self.down[format(key)] = format(key);
        #print('{0} pressed'.format(key))

    def on_release(self, key):
        if(format(key) in self.pressed):
            del self.pressed[format(key)]
        self.realesed[format(key)] = format(key);

        
        #print('{0} released'.format(key))
        if(self.running == False):
            return False;

    def updateKeys(self):
        self.realesed = {};
        for key in self.down:
            self.pressed[key] = key;
        self.down = {};


inputh= inputHandler(1, True)
inputh.start();

# value = input("test : ");
# print(value , "sdasdasd")

while(True):
    sleep(0.5)
    if(input("exit") == "y"):
        inputh.running = False;
        break;

inputh.running = False;