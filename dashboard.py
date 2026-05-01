from flask import Flask, render_template_string
import datetime
import nmap

app = Flask(__name__)

def scan_network():
    try:
        scanner = nmap.PortScanner()
        scanner.scan(hosts="192.168.1.0/24", arguments="-sn")
        found = []
        for host in scanner.all_hosts():
            found.append({"ip": host, "state": scanner[host].state()})
        return found
    except:
        return []

@app.route("/")
def index():
    scanned = scan_network()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    html = """
    <html>
    <head><title>Network Monitor</title></head>
    <body style="font-family:arial; padding:20px; background:#111; color:white;">
    
    <h1>Network Monitor</h1>
    <p>Last scan: {{ timestamp }}</p>
    
    <h2>Local Network Devices</h2>
    {% if scanned %}
        {% for s in scanned %}
        <p style="color:lightblue">{{ s.ip }} — {{ s.state }}</p>
        {% endfor %}
    {% else %}
        <p style="color:gray">No devices found — connect to WiFi to scan local network</p>
    {% endif %}
    
    </body>
    </html>
    """
    return render_template_string(html, scanned=scanned, timestamp=timestamp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
