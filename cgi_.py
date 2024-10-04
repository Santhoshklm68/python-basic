import socket

# Create a TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get input from the user
host = input("Enter server IP: ")
port = int(input("Enter port: "))

# Connect to the server
s.connect((host, port))
print(f"Connected to {host}:{port}")

# Sending a message to the server
message = "Hello, Server!"
s.sendall(message.encode('utf-8'))

# Receiving a response from the server
response = s.recv(135)
print("Server response:", response.decode('utf-8'))

