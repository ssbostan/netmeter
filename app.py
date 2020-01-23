#!/usr/bin/python3

import sys
import netmeter

try:
    if(len(sys.argv)!=2):
        print("Usage: netmeter.py <interface>")
    else:
        while(True):
            RX=netmeter.getRX(sys.argv[1])
            TX=netmeter.getTX(sys.argv[1])
            print(f"RX: {RX[0]//1024} KB/s, {RX[1]} PKT/s | TX: {TX[0]//1024} KB/s, {TX[1]} PKT/s")
            
except(IOError, PermissionError):
    print("Error...")
except KeyboardInterrupt:
    print("\nExit with Keyboard Interrupt...")
