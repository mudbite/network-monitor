from flask import Flask, render_template_string
import datetime
import subprocess

app = Flask(__name__)

devices = ["google.com", "8.8.8.8", "192.168.1.1"]

def ping(host):
    result = subprocess.run(
        ["ping", "-c", "1", host],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    return result.returncode == 0

@app.route("/")
def index():
    results = []
    for device in devices:
        status = "ONLINE" if ping(device) else "OFFLINE"
        color = "green" if status == "ONLINE" else "red"
        results.append({"device": device, "status": status, "color": color})
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    html = """
    <html>
    <head><title>Network Monitor</title></head>
    <body style="font-family:arial; padding:20px; background:#111; color:white;">
    <h1>Network Monitor</h1>
    <p>Last scan: {{ timestamp }}</p>
    {% for r in results %}
    <p style="color:{{ r.color }}">{{ r.device }} — {{ r.status }}</p>
    {% endfor %}
    </body>
    </html>
    """
    return render_template_string(html, results=results, timestamp=timestamp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

