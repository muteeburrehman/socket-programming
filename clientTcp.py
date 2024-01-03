import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server address and port
server_address = ('localhost', 12345)

# Connect to the server
client_socket.connect(server_address)
print('Connected to', server_address)

# Send data to server
message = 'Hello, server!'
client_socket.send(message.encode('utf-8'))

# Receive data from the server
data = client_socket.recv(1024)
print('Received response from the server:', data.decode('utf-8'))

# Close the connection
client_socket.close()