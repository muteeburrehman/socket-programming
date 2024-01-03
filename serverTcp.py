import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Create a connection
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Listen for a incoming connection
server_socket.listen(1) # we allow a max 1 connection in this case

print('TCP server is listening {}:{}'.format(*server_address))

# Wait for a connection
print('Waiting for connection...')
client_socket, client_address = server_socket.accept()
print('Connected to', client_address)

# Receive data from the client
data = client_socket.recv(1024)
print('Received data from the client:', data.decode('utf-8'))

# Send response back to client
response = 'Hello, client'
client_socket.sendall(response.encode('utf-8'))

# close the connections
client_socket.close()
server_socket.close()