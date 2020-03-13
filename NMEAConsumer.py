"""
Broker programme for UDP IPv4
By: JOR
    v0.1    12SEP18     Forked from SDNode AUTH2.py
"""

import socket
import statistics
from GPS.GNS import GNS_Talker
from GPS.Quality import GNSQuality
from NMEA.Sentence import NMEA_Sentence
from UDP.Utilities import find_local_host_ipv4


# Instantiate NMEA Instrument objects
myTalker = NMEA_Sentence()
myGNS3001 = GNS_Talker(3001)
myGNS3002 = GNS_Talker(3002)
myGNS3003 = GNS_Talker(3003)

# instantiate quality objects
myGNSQuality3001 = GNSQuality()
myGNSQuality3002 = GNSQuality()
myGNSQuality3003 = GNSQuality()

# Set up parameters for NMEAConsumer, find the IPv4 address on the correct subnet
NMEAConsumer_IPv4 = find_local_host_ipv4('192.168.5.10')
NMEAConsumer_Port = 3000

# Create a UDP socket
NMEAConsumerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = (NMEAConsumer_IPv4, NMEAConsumer_Port)
print('starting NMEAConsumer on {} port {}'.format(*server_address))
sock.bind(server_address)

sentence = ''

while True:
    print('\nWaiting to receive message')
    data, address = sock.recvfrom(4096)

    print('Received {} bytes from {}:'.format(len(data), address[0]), address[1])
    gps_device = str(address[1])

    if data:
        sentence = data.decode('utf-8')
        myTalker.sentence = sentence
        if myTalker.parse_talker():
            print('Instrument is a {}'.format(myTalker.InstrumentName))
            if myTalker.parse_full_sentence(sentence):
                print('Sentence type is {}'.format(myTalker.sentence_id))

    if gps_device == '3001':
        myGNS3001.parse_gns(sentence)
        myGNSQuality3001.add_values(myGNS3001.Longitude, myGNS3001.Latitude)
        myGNSQuality3001.run()

    if gps_device == '3002':
        myGNS3002.parse_gns(sentence)
        myGNSQuality3002.add_values(myGNS3002.Longitude, myGNS3002.Latitude)
        myGNSQuality3002.run()

    if gps_device == '3003':
        myGNS3003.parse_gns(sentence)
        myGNSQuality3003.add_values(myGNS3003.Longitude, myGNS3003.Latitude)
        myGNSQuality3003.run()

