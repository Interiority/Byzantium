"""
    Utilities for Byzantium
    By: JOR
    v0.1    18AUG18     Alpha
"""

import time
from random import random

center_latitude_int = '5510'
center_longitude_int ='726'
center_latitude_fraction = 879
center_longitude_fraction =.10786


def randomize_lat(scaling):
    # Generate a random number between 0 and 1
    a = random()
    # Multiply it by a scaling factor to specify how noisy the signal is
    b = a / scaling
    # Use this to make the fraction part of the latitude noisy
    c = center_latitude_fraction * (b + 1)
    # 6 significant places
    d = c/100000
    # Format it to 6 digits
    noisy_latitude_fraction = '{0:.6f}'.format(d)
    latitude = center_latitude_int + str(noisy_latitude_fraction)
    return latitude


def randomize_long(scaling):
    # Generate a random number between 0 and 1
    a = random()
    # Multiply it by a scaling factor to specify how noisy the signal is
    b = a / scaling
    # Use this to make the fraction part of the longitude noisy
    c = center_latitude_fraction * (b + 1)
    # 6 significant places
    d = c / 100000
    # Format it to 6 digits
    noisy_longitude_fraction = '{0:.6f}'.format(d)
    longitude = center_latitude_int + str(noisy_longitude_fraction)
    return longitude
