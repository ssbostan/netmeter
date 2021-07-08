from flask import Flask

from netmeter import get_iface_list, get_iface_raw_data

app = Flask(__name__)

app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True

@app.route("/")
def index():
    network_stats = {}
    iface_list = get_iface_list()
    for iface in iface_list:
        iface_receive = get_iface_raw_data(iface, "rx")
        iface_transmit = get_iface_raw_data(iface, "tx")
        network_stats[iface] = {
            "receive_bytes": iface_receive[0],
            "receive_packets": iface_receive[1],
            "transmit_bytes": iface_transmit[0],
            "transmit_packets": iface_transmit[1]
        }
    return network_stats

if __name__ == "__main__":
    app.run()
