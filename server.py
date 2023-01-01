#!/bin/python3.9
import socket
import sys

s = socket.socket()
s.bind(("127.0.0.1",9000)) #Change these
s.listen(10)
i=1

while True:
    sc, address = s.accept()
    print address
    f = open('files.zip','wb') #open in binary
    l = 1
    while(l):
        l = sc.recv(1024)
        while (l):
            f.write(l)
            l = sc.recv(1024)
        f.close()
        sc.send("received") # Would like to send back a response

    sc.close()

s.close()
