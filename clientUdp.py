import socket

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address and port
server_address = ('localhost', 6789)

# Send data to the server
message = 'Hello, server!'
client_socket.sendto(message.encode(), server_address)

# Receive data from the server
data, server_address = client_socket.recvfrom(1024)

# Print the received response
print("Received response from {}:{}".format(server_address, data.decode()))

# Close the socket
client_socket.close()