# Wake-on-LAN
Python script for Wake on LAN


### Usage
```bash
python wakeon.py [<mac address>][<broadcast address>]
```
The first parameter is the MAC address of the targeted device to be woken up.
The second parameter is IP adress of the targeted device to be woken up.
Both parameter are optional as if left empty, the program would ask the user to input both the MAC and IP address 

Example
```bash
python wakeon.py 12:23:34:45:56:67 127.0.0.1
```

___

### Extra

This script is only meant for testing to see if the targeted computer reveiced the magic packet while it is ON
It also translate the magic packet into human readable Hexadecimal format

### Usage
```bash
python sniff.py
```

References

