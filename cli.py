from sys import argv, exit
from prettytable import PrettyTable

from netmeter import get_iface_stats

output = PrettyTable(
    ["Receive KB/s", "Receive Packet/s", "Transmit KB/s", "Transmit Packet/s"]
)

if len(argv) != 2:
    print("Usage: python3 cli.py <interface>")
    exit(1)

try:
    while True:
        receive_per_second = get_iface_stats(argv[1], "rx")
        transmit_per_second = get_iface_stats(argv[1], "tx")
        output.add_rows(
            [
                [
                    receive_per_second[0] // 1024,
                    receive_per_second[1],
                    transmit_per_second[0] // 1024,
                    transmit_per_second[1]
                ]
            ]
        )
        print(f"{output}\x1b[5A")
        output.clear_rows()
except (IOError, PermissionError):
    print("Error: Interface not found or access is denied.")
    exit(1)
except KeyboardInterrupt:
    print("\x1b[5B")
    exit(0)
