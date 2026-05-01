import nmap
import datetime
import time

def scan_network():
    scanner = nmap.PortScanner()
    network = "192.168.1.0/24"
    
    while True:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\n--- Network Scan at {timestamp} ---")
        print(f"Scanning {network}...")
        
        scanner.scan(hosts=network, arguments="-sn")
        
        hosts = scanner.all_hosts()
        if hosts:
            for host in hosts:
                state = scanner[host].state()
                print(f"Device: {host} — {state}")
        else:
            print("No devices found. Connect to WiFi first.")
        
        print("\nNext scan in 60 seconds... (Volume Down + C to stop)")
        time.sleep(60)

scan_network()
