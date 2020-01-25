
# Copyright (c) 2020, Saeid Bostandoust
# All rights reserved.

from time import sleep

def getNetInfo(iface, ctype):
    with open(f"/sys/class/net/{iface}/statistics/{ctype}_bytes", "r") as mfile:
        cbytes=mfile.read()
    with open(f"/sys/class/net/{iface}/statistics/{ctype}_packets", "r") as mfile:
        cpackets=mfile.read()
    return (int(cbytes), int(cpackets))
    
def getRX(iface):
    T1=getNetInfo(iface, "rx")
    sleep(1)
    T2=getNetInfo(iface, "rx")
    return (T2[0]-T1[0], T2[1]-T1[1])
    
def getTX(iface):
    T1=getNetInfo(iface, "tx")
    sleep(1)
    T2=getNetInfo(iface, "tx")
    return (T2[0]-T1[0], T2[1]-T1[1])
