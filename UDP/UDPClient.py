import socket
from socket import *
import sys
import threading
import time

"""
    UDP for IPv4
    By: JOR
    v0.1    12SEP18     Forked from SDNode
"""


class UDPClient(threading.Thread):
    def __init__(self, thread_id, name, udp_socket):
        threading.Thread.__init__(self)
        self.socket = udp_socket
        self.name = name
        self.thread_id = thread_id
        self.NMEAConsumer_IPv4 = '192.168.234.145'
        self.NMEAConsumer_Port = 3000

    def run(self):
        print("Starting thread " + str(self.thread_id) + " - " + self.name + "\n")

    def send(self, bytes_to_send):
        try:
            self.socket.sendto(bytes_to_send, (self.NMEAConsumer_IPv4, self.NMEAConsumer_Port))
        except socket.error as msg:
            sys.stderr.write('UDP Client: {}\n'.format(msg))
        finally:
            start_time = time.time()

