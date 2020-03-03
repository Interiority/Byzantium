"""
    Sentence
    By: JOR
    v0.1    20SEP18     Forked from Survey
"""

from GPS.Instrument import Generic0183


class NMEA_Sentence(Generic0183):
    def __init__(self):        # Init for instances
        Generic0183.__init__(self)

    def parse_full_sentence(self, nmea_full_sentence):
        # Uncomment for diagnostics
        # print('[GPS-parse] Parsing GPS sentence = ' + nmea_full_sentence)
        list_of_values = nmea_full_sentence.split(',')
        # Get the sentence ID
        sentence_id = list_of_values[0][3:]

        try:
            if sentence_id == 'GNS':
                self.InstrumentName = 'GNS'
                self.InstrumentManufacturer = 'Unknown'
                return True
            else:
                self.InstrumentName = ''
                print('Unknown GPS sentence - ' + nmea_full_sentence)
                return False
        except ValueError:
            print('[GPS-parse] Error parsing sentence')
            return False
