import socket

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 6789)
server_socket.bind(server_address)

print("UDP server is listening on {}:{}".format(*server_address))

while True:
    # Receive data and address of the client
    data, client_address = server_socket.recvfrom(1024)

    # Print received data and client address
    print("Received data from {}:{}".format(client_address, data.decode()))

    # Send a response back to the client
    response = 'Hello Client!'
    server_socket.sendto(response.encode(), client_address)

