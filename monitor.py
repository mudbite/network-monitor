import subprocess
import datetime
import time

devices = ["google.com", "8.8.8.8", "192.168.1.1"]

def ping(host):
    result = subprocess.run(
        ["ping", "-c", "1", host],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    return result.returncode == 0

def monitor():
    while True:
        with open("log.txt", "a") as log:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"\n--- Scan at {timestamp} ---")
            for device in devices:
                status = "ONLINE" if ping(device) else "OFFLINE"
                line = f"{timestamp} | {device} | {status}"
                print(line)
                log.write(line + "\n")
        print("\nNext scan in 30 seconds... (Ctrl+C to stop)")
        time.sleep(30)

monitor()

