#!/usr/bin/python3
#Wake on LAN Python Script
import sys
import re
import struct
import socket

#Class to validate IP address and MAC address entered by the user
class Validation():
    def validate_MAC(self, addressMAC):
        #Pattern to validate the MAC address
        regex = ("^([0-9A-Fa-f]{2}[:]){5}([0-9A-Fa-f]{2})$")
        
        format = re.compile(regex)
        
        if(re.search(format, addressMAC)):
            print("MAC Address entered is ", addressMAC)
        else:
            print("Invalid MAC Address!")
            sys.exit()
            
    def validate_IP(self, addressIP):
        #Pattern to validate the IP address
        regex = ("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
        
        format = re.compile(regex)
        
        if(re.search(format, addressIP)):
            print("IP Address entered is ", addressIP)
        else:
            print("Invalid IP Address!")
            sys.exit()

#Class for Wake on LAN
class Woke():
    def awaken(self, addressMAC, addressIP, port):
        #This would split the MAC address value into a list 
        separateMAC = str.split(addressMAC,':')
        #This would pack the separateMAC value into bytes form
        hexaAddress = struct.pack("BBBBBB", 
                             int(separateMAC[0], 16),
                             int(separateMAC[1], 16),
                             int(separateMAC[2], 16),
                             int(separateMAC[3], 16),
                             int(separateMAC[4], 16),
                             int(separateMAC[5], 16))
    
        #Concatenating all the content required for the magic packet
        self.packet = b'\xff' * 6 + hexaAddress * 16
        #Opening, sending and closin of packet
        s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(self.packet,(addressIP, port))
        s.close()
        
        print ("\nPacket has been send to ", addressMAC)
        print ("With IP address ", addressIP)
        
                
argnum = len(sys.argv)
#Allow the user to enter commmand line arguments when running the python script
if(argnum > 3):
    print("\nInvalid arguments passed to the program!")
    sys.exit()
    
elif(argnum < 2):
    print("\nEnter the MAC address of the device to be woken up. (In this format: aa:aa:aa:aa:aa:aa)")
    addressMAC = input("MAC Address: ")
    valid = Validation()
    valid.validate_MAC(addressMAC)
    print("\nEnter the IP address of the device to be woken up. (In this format: x.x.x.x)")
    addressIP = input("IP Address: ")
    valid.validate_IP(addressIP)

elif(argnum < 3):
    valid = Validation()
    valid.validate_MAC(sys.argv[1])
    addressMAC = sys.argv[1]
    print("\nEnter the IP address of the device to be woken up. (In this format: x.x.x.x)")
    addressIP = input("IP Address: ")
    valid.validate_IP(addressIP)
    
elif(argnum == 3):
    valid = Validation()
    valid.validate_MAC(sys.argv[1])
    addressMAC = sys.argv[1]
    valid.validate_IP(sys.argv[2])
    addressIP = sys.argv[2]
    
#Waking up computer    
wakeup = Woke()
wakeup.awaken(addressMAC, addressIP, 9)
