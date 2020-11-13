import os
#import imp
__path__ = os.getcwd()

#
# def reload_func():
#     imp.reload(graphics)
#     threading.Timer(1, reload_func).start()
#
# reload_func()

pythonname = ""

from sys import platform
if platform == "linux" or platform == "linux2":
    pythonname = "python3.9"
    # linux
elif platform == "darwin": pass
    # OS X
elif platform == "win32":
    pythonname = "python"
    # Windows...

command = pythonname + " ./TERRANIMATION/terranimation.py"

print("command result: " + str(os.system(command)))
#print(os.system("pause"))