import os
import imp
__path__ = os.getcwd()

import threading

from TERRANIMATION import graphics

def reload_func():
    imp.reload(graphics)
    threading.Timer(1, reload_func).start()

reload_func()

command = "python3.9 ./TERRANIMATION/terranimation.py"

print("command result: " + str(os.system(command)))
#print(os.system("pause"))