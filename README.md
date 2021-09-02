# netmeter

![Visits Badge](https://badges.pufler.dev/visits/ssbostan/netmeter)

If you are looking for a tool to monitor your network interfaces, here you are.

See [netmeter-exporter](https://github.com/ssbostan/netmeter-exporter) to export Prometheus metrics.

## Installation and usage:

You can run netmeter either on localhost or with a docker image.

### Docker:

```bash
docker run -d --name netmeter -p 8080:8080 -v /sys:/host/sys:ro -e NETMETER_SYS_PATH=/host/sys ssbostan/netmeter:2
```

![demo](https://raw.githubusercontent.com/ssbostan/netmeter/master/demo.gif)

### Localhost:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python web.py
```

### CLI usage:

`cli.py` is a simple app to show an interface per second stats.

```
python cli.py <interface>
```

## How to contribute:

All contributions are accepted. Fork it and develop it.

### TODO:

  - [ ] Collect more network statistics
