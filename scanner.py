import socket

target = "127.0.0.1"

def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.1) # Shorter timeout makes the scan faster
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"\n[!] Port {port} is OPEN")
    s.close()

print(f"Scanning {target} from port 1 to 1024...")

# This will loop through every number from 1 to 1024
for port in range(1, 1025):
    # Print a small progress update every 100 ports
    if port % 100 == 0:
        print(f"Progress: Checking port {port}...")
    scan_port(port)

print("\nScan complete.")