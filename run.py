import os
from sys import platform

#import imp
__path__ = os.getcwd()

#
# def reload_func():
#     imp.reload(graphics)
#     threading.Timer(1, reload_func).start()
#
# reload_func()


if platform == "linux" or platform == "linux2":
    command = "python3.9 ./TERRANIMATION/terranimation.py"
elif platform == "darwin":
    pass
    # OS X
elif platform == "win32":
    command = "python ./TERRANIMATION/terranimation.py"


print("command result: " + str(os.system(command)))
#print(os.system("pause"))