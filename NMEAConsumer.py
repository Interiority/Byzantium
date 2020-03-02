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
print('Starting NMEAConsumer')

# Bind the socket
try:
    NMEAConsumerSocket.bind((NMEAConsumer_IPv4, NMEAConsumer_Port))
except socket.error as msg:
    sys.stderr.write('Bind failure warning: {}\n'.format(msg) + "\n")
finally:
    print(socket)

# Loop to wait for data
try:
    while 1:
        data, address = NMEAConsumerSocket.recvfrom(1024)
        # record the source of the packet
        client_ipv4, client_port = address
        # read the data
        read_buffer = data
except socket.error as msg:
    sys.stderr.write('UDP socket warning: {}\n'.format(msg) + "\n")
