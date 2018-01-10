import socket
host = "127.0.0.1"
port = 12345
data = "test"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    s.sendall(b"testing")
    data = s.recv(1024)
print("recieved", repr(data))