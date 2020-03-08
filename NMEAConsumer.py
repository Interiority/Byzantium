"""
Broker programme for UDP IPv4
By: JOR
    v0.1    12SEP18     Forked from SDNode AUTH2.py
"""

import socket
import statistics
from GPS.GNS import GNS_Talker
from NMEA.Sentence import NMEA_Sentence
from UDP.Utilities import find_local_host_ipv4

# Set up lists for storing data
GNS3001_Latitudes = []
GNS3001_Longitudes = []


# Instantiate NMEA Instrument objects
myTalker = NMEA_Sentence()
myGNS3001 = GNS_Talker(3001)
myGNS3002 = GNS_Talker(3002)
myGNS3003 = GNS_Talker(3003)

NMEAConsumer_IPv4 = find_local_host_ipv4('192.168.234.2')
NMEAConsumer_Port = 3000
NMEAConsumerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Create a UDP socket
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
        GNS3001_Latitudes.append(myGNS3001.Latitude)
        GNS3001_Longitudes.append(myGNS3001.Longitude)
        latitude_median = statistics.median(GNS3001_Latitudes)
        longitude_median = statistics.median(GNS3001_Longitudes)
        if latitude_median != myGNS3001.Latitude or longitude_median != myGNS3001.Longitude:
            print('GNS3001 is broken')
    if gps_device == '3002':
        myGNS3002.parse_gns(sentence)
    if gps_device == '3003':
        myGNS3003.parse_gns(sentence)




