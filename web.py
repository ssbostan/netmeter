#!/usr/bin/python3

# Copyright (c) 2020, Saeid Bostandoust
# All rights reserved.

from flask import Flask

import netmeter
import json

app = Flask(__name__)

class AutoVivification(dict):
    """Implementation of perl's autovivification feature."""
    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)

        except KeyError:
            value = self[item] = type(self)()
            return value


@app.route("/<iface>/")
def main(iface):
    DATA=AutoVivification()
    try:
        rx=netmeter.getRX(iface)
        tx=netmeter.getTX(iface)
        DATA[iface]["rx"]["bytes"]=rx[0]
        DATA[iface]["rx"]["packets"]=rx[1]
        DATA[iface]["tx"]["bytes"]=tx[0]
        DATA[iface]["tx"]["packets"]=tx[1]

    except(IOError, PermissionError):
        DATA[iface]=None

    finally:
        return json.dumps(DATA, indent=2)


if __name__ == "__main__" :
    app.run()
