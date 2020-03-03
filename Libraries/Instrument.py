"""
    Generic 0183 Instrument
    By: JOR
    v0.1    20SEP18     Forked from Survey
"""


class Generic0183:
    def __init__(self):        # Init for instances
        self.InstrumentName = 'Unknown'
        self.InstrumentManufacturer = 'Unknown'
        self.NewMeasurement = False
        self.MeasurementValid = False
