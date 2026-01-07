import socket

# Target is your own computer for safe practice
target = "127.0.0.1" 

def scan_port(port):
    try:
        # 'with' statement ensures the socket closes after the block
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5) 
            result = s.connect_ex((target, port))
            
            if result == 0:
                print(f"\n[!] Port {port} is OPEN")
                # Try to capture the 'Secret Flag'
                try:
                    data = s.recv(1024)
                    if data:
                        print(f"    [+] Data Received: {data.decode().strip()}")
                except socket.timeout:
                    print("    [-] No data received (Timeout)")
    except Exception as e:
        print(f"\n[!] Error: {e}")

print(f"--- Starting Scan on {target} ---")
# We scan specifically around the port our server is using
for port in range(9990, 10001):
    print(".", end="", flush=True)
    scan_port(port)

print("\n\n--- Scan Finished ---")