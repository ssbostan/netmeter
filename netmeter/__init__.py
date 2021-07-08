from os import environ, listdir, path
from time import sleep

NET_PATH = path.join(environ.get("NETMETER_SYS_PATH", "/sys"), "class/net")

def get_iface_list():
    return listdir(NET_PATH)

def get_iface_raw_data(iface, ctype):
    with open(f"{NET_PATH}/{iface}/statistics/{ctype}_bytes", "r") as f:
        iface_bytes = f.read()
    with open(f"{NET_PATH}/{iface}/statistics/{ctype}_packets", "r") as f:
        iface_packets = f.read()
    return int(iface_bytes), int(iface_packets)

def get_iface_stats(iface, ctype):
    current_value_t1 = get_iface_raw_data(iface, ctype)
    sleep(1)
    current_value_t2 = get_iface_raw_data(iface, ctype)
    return (
        current_value_t2[0] - current_value_t1[0],
        current_value_t2[1] - current_value_t1[1]
    )
