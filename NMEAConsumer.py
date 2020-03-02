"""
Broker programme for UDP IPv4
By: JOR
    v0.1    12SEP18     Forked from SDNode AUTH2.py
"""

import time
import sys
import socket
from Libraries import UDP, Utilities

NMEAConsumer_IPv4 = '192.168.234.145'
NMEAConsumer_Port = 3000
NMEAConsumerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = (NMEAConsumer_IPv4, NMEAConsumer_Port)
print('starting NMEAConsumer on {} port {}'.format(*server_address))
sock.bind(server_address)

while True:
    print('\nwaiting to receive message')
    data, address = sock.recvfrom(4096)

    print('received {} bytes from {}'.format(
        len(data), address))
    print(data)

    if data:
        sent = sock.sendto(data, address)
        print('sent {} bytes back to {}'.format(
            sent, address))
