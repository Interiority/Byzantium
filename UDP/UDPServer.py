import socket
from socket import *
import sys
import threading

"""
    UDP for IPv4
    By: JOR
    v0.1    12SEP18     Forked from SDNode
"""


class UDPServer(threading.Thread):
    def __init__(self, thread_id, name, udp_socket):
        threading.Thread.__init__(self)
        self.socket = udp_socket
        self.name = name
        self.thread_id = thread_id
        self.server_ipv4 = ""
        self.server_port = 3001
        self.client_ipv4 = ""
        self.client_port = 3000
        self.read_buffer = []
        self.write_buffer = []

    def run(self):
        print("Starting thread " + str(self.thread_id) + " - " + self.name + "\n")
        # Bind the socket
        try:
            self.socket.bind((self.server_ipv4, self.server_port))
        except socket.error as msg:
            sys.stderr.write('Bind failure warning: {}\n'.format(msg) + "\n")
        finally:
            print(self.socket)

        # Loop to wait for data
        try:
            while 1:
                data, address = self.socket.recvfrom(1024)
                # record the source of the packet
                self.client_ipv4, self.client_port = address
                # read the data
                self.read_buffer = data
        except socket.error as msg:
            sys.stderr.write('UDP socket warning: {}\n'.format(msg) + "\n")
        except Exception as error:
            print("UDP socket unexpected error:", sys.exc_info()[0])

    def write_udp(self, destination_ipv4, destination_port):
        try:
            bytes_to_send = self.write_buffer
            self.socket.sendto(bytes_to_send, (destination_ipv4, destination_port))
        except socket.error as msg:
            sys.stderr.write('UDP Client: {}\n'.format(msg))