import os

__path__ = os.getcwd()

command = "python3.9 ./TERRANIMATION/terranimation.py"

print("command result: " + str(os.system(command)))
#print(os.system("pause"))