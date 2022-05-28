#!/usr/bin/python3

import socket
import struct
import sys
import re

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("", 9))

while True:
    #Retrieving any data sent from the IP address entered previously
    data, address = sock.recvfrom(4096)
    #All of below commands are to translate the data received into hexadecimal form for easy read
    print("\nThe source IP address and the port", address)
    print("\n")
    reformat = struct.unpack("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB", data)
    inttohex = list(reformat)
    
    for i in range(0,102):
        inttohex[i] = hex(inttohex[i]).lstrip("0x").rstrip("L")
        
    msglist = []
    
    for n in range(0,97,6):
        msglist.append((inttohex[n:n+6]))
    
    for j in range(0, 17):
        k = 0
        msg = ":".join([msglist[j][k], msglist[j][k+1], msglist[j][k+2], msglist[j][k+3], msglist[j][k+4], msglist[j][k+5]])
        print(msg)
    
    if(msg != 0):
        confirm = input("\nAre you done? or do you want to continue? Enter yes to continue and anything to exit.\nPrompt: ")
        if(confirm != "yes"):
            sock.close()
            sys.exit()