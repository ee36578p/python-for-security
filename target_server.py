import socket

host = "127.0.0.1"
port = 9999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # THIS LINE PREVENTS THE 'ADDRESS ALREADY IN USE' ERROR
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    s.bind((host, port))
    s.listen(1)
    print(f"Server ACTIVE on port {port}. Waiting for hacker...")
    
    conn, addr = s.accept()
    with conn:
        print(f"Connection received from {addr}")
        conn.sendall(b"CONGRATS! You found the secret flag: {PY_HACKER_101}")