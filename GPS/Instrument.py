"""
    Generic 0183 Instrument
    By: JOR
    v0.1    20SEP18     Forked from Survey
"""


class Generic0183:
    def __init__(self):        # Init for instances
        self.InstrumentName = 'Unknown'
        self.InstrumentManufacturer = 'Unknown'
        self.sentence = ''

        self.sentence_id = ''

    def parse_talker(self):
        list_of_values = self.sentence.split(',')
        # Get the talker ID
        self.sentence_id = list_of_values[0][1:-3]

        if list_of_values[0][1:-4] == 'P':  # Found a proprietary instrument
            if list_of_values[0][1:-3] == 'PG':
                self.InstrumentName = 'GPS'
                self.InstrumentManufacturer = 'Garmin'
            else:
                self.InstrumentName = 'Proprietary'
            return True
        elif self.sentence_id == 'GA':  # Found a sensor with Galileo data
            # print("Found a Galileo")
            self.InstrumentName = 'Galileo GPS'
            return True
        elif self.sentence_id == 'GB' or self.sentence_id == 'BG':  # Found a sensor with BeiDou data
            # print("Found a BeiDou")
            self.InstrumentName = 'Beidou GPS'
            return True
        elif self.sentence_id == 'GP':  # Found a sensor with GPS data
            # print("Found a GPS")
            self.InstrumentName = 'Generic GPS'
            return True
        elif self.sentence_id == 'GL':  # Found a sensor with GPS data
            # print("Found a GLONASS")
            self.InstrumentName = 'GLONASS GPS'
            return True
        elif self.sentence_id == 'GN':  # Found a sensor with mixed GPS and GLONASS data
            # print("Found a GPS with mixed data")
            self.InstrumentName = 'GNSS GPS'
            return True
        else:
            print("[M2] - No idea what this talker is" + self.sentence)
            print(list_of_values[0][1:-3])
            return False
