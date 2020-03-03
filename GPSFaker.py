"""
Broker programme for Byzantium GPS
By: JOR
    v0.1    12SEP18     Forked from SDNode COMM2.py
"""
from UDP.Utilities import seconds_later, return_local_time, find_local_ipv4, return_gps_time
from Byz.ByzUtilities import randomize_lat, randomize_long
from UDP.UDPClient import UDPClient
import socket
import sys
import time

# Exit if localhost = 127.0.0.1
local_host_ip = find_local_ipv4()

NMEAConsumer_IPv4 = '192.168.234.145'
NMEAConsumer_Port = 3000

print("Main thread started - GPSFaker")

ThreadName = 'GPS1'
GPSSocket1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
gps1 = UDPClient(1, ThreadName, GPSSocket1)

try:
    gps1.server_ipv4 = local_host_ip
    gps1.setDaemon(True)
    gps1.start()
except socket.error as msg:
    sys.stderr.write('Socket error starting UDP server: {}\n'.format(msg) + "\n")
finally:
    print("gps1 sending")

ThreadName = 'GPS2'
GPSSocket2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
gps2 = UDPClient(2, ThreadName, GPSSocket1)

try:
    gps2.server_ipv4 = local_host_ip
    gps2.setDaemon(True)
    gps2.start()
except socket.error as msg:
    sys.stderr.write('Socket error starting UDP server: {}\n'.format(msg) + "\n")
finally:
    print("gps2 sending")

ThreadName = 'GPS3'
GPSSocket2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
gps3 = UDPClient(3, ThreadName, GPSSocket1)

try:
    gps3.server_ipv4 = local_host_ip
    gps3.setDaemon(True)
    gps3.start()
except socket.error as msg:
    sys.stderr.write('Socket error starting UDP server: {}\n'.format(msg) + "\n")
finally:
    print("gps2 sending")

# Initialize the 1 second timer
start_time = time.time()

while 1:
    # if X seconds have elapsed, send a NMEA sentence
    if seconds_later(start_time, 1):
        local_time = return_local_time()
        try:

            gps_time = return_gps_time()

            lat = randomize_lat(1000)
            long = randomize_long(1000)
            gngns = '$GNGNS,{},{},N,{},W,FF,19,0.65,111.2,53.9,1.0,0000*52'.format(gps_time, lat, long)
            bytes_to_send = gngns.encode()
            time.sleep(.2)
            gps1.send(bytes_to_send)
            print('At {} GPS1 sent {}'.format(local_time, bytes_to_send))

            lat = randomize_lat(1000)
            long = randomize_long(1000)
            gngns = '$GNGNS,{},{},N,{},W,FF,19,0.65,111.2,53.9,1.0,0000*52'.format(gps_time, lat, long)
            bytes_to_send = gngns.encode()
            time.sleep(.2)
            gps2.send(bytes_to_send)
            print('At {} GPS2 sent {}'.format(local_time, bytes_to_send))

            lat = randomize_lat(1000)
            long = randomize_long(1000)
            gngns = '$GNGNS,{},{},N,{},W,FF,19,0.65,111.2,53.9,1.0,0000*52'.format(gps_time, lat, long)
            bytes_to_send = gngns.encode()
            time.sleep(.2)
            gps3.send(bytes_to_send)
            print('At {} GPS3 sent {}'.format(local_time, bytes_to_send))

        except socket.error as msg:
            sys.stderr.write('UDP Client: {}\n'.format(msg))
        finally:
            start_time = time.time()
