import os

__path__ = os.getcwd()

command = "py .\\TERRANIMATION\\terranimation.py"

print("command result: " + str(os.system(command)))
#print(os.system("pause"))