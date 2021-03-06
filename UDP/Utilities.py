"""
    Utilities for UDP for IPv4
    By: JOR
    v0.1    12SEP18     Forked from SDNode
"""

import socket
import time


def find_local_host_ipv4(server_to_test_against):
    """
    Figure out what your IPv4 address is on a particular interface
    :param server_to_test_against:
    :return: the source host IPv4 address
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((server_to_test_against, 80))
    local_ipv4 = (s.getsockname()[0])
    s.close()
    return local_ipv4


def find_local_ipv4():
    local_host_ip = str(socket.gethostbyname(socket.gethostname()))
    if local_host_ip == '127.0.0.1':
        print("You must set the hostname correctly in /etc/hosts!")
        print("Existing until you sort this!!")
        exit(0)
    return local_host_ip


def return_local_time():
    local_time = time.localtime()  # get struct_time
    time_string = time.strftime("%H:%M:%S", local_time)
    return time_string


def return_gps_time():
    local_time = time.localtime()  # get struct_time
    time_string = time.strftime("%H%M%S", local_time)
    return time_string


def seconds_later(event, how_many_seconds):
    return event + how_many_seconds < time.time()


