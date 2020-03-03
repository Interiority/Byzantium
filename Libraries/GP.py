"""
    GPS Parser
    By: JOR
    v0.1    20SEP18     Forked from Survey
"""

from Libraries.TalkerID import Talker


class GPS(Talker):
    def __init__(self):        # Init for instances
        super().__init__()
        self.LatitudeDM = ''
        self.LatitudeDD = 55.0000
        self.NSHemisphere = 'N'
        self.LongitudeDM = ''
        self.LongitudeDD = 7.0000
        self.EWHemisphere = 'W'
        self.GPSTime = '000000'
        self.GPSDate = '230465'
        self.FixType = ''
        self.FixQuality = 0
        self.Altitude = 0
        self.NumberOfSatellitesInView = 0
        self.HDOP = 0
        self.VDOP = 0
        self.PDOP = 0
        self.TrackMadeGoodTrue = 0
        self.TrackMadeGoodMagnetic = 0
        self.GroundSpeedKnots = 0
        self.GroundSpeedKMH = 0
        self.MagneticVariation = 0
        self.MagneticVariationHemisphere = 0
        self.NumberOfSatellitesBeingTracked = 0
        self.Altitude = 0
        self.HeightOfGeoid = 0

    def parse(self, nmea_full_sentence):
        # Uncomment for diagnostics
        # print('[GPS-parse] Parsing GPS sentence = ' + nmea_full_sentence)
        list_of_values = nmea_full_sentence.split(',')
        # Get the sentence ID
        sentence_id = list_of_values[0][3:]

        try:
            if sentence_id == 'GGA':
                print('Found a GGA')
                self.parse_gga(nmea_full_sentence)
            elif sentence_id == 'GLL':
                print('Found a GLL but will not process')
                #self.parse_gll(nmea_full_sentence)
            elif sentence_id == 'GSA':
                print('Found a GSA but will not process')
                #self.parse_gsa(nmea_full_sentence)
            elif sentence_id == 'GSV':
                print('Found a GSV but will not process')
                #self.parse_gsv(nmea_full_sentence)
            elif sentence_id == 'RMC':
                print('Found a RMC but will not process')
                #self.parse_rmc(nmea_full_sentence)
            elif sentence_id == 'GGA':
                print('Found a GGA but will not process')
                #self.parse_gga(nmea_full_sentence)
            elif sentence_id == 'VTG':
                print('Found a VTG  but will not process')
                #self.parse_vtg(nmea_full_sentence)
            elif sentence_id == 'RMB':
                print('Found a RMB but will not process')
            elif sentence_id == 'GBS':
                print('Found a GBS but will not process')
            elif sentence_id == 'GNS':
                print('Found a GNS but will not process')
            elif sentence_id == 'GRS':
                print('Found a GRS but will not process')
            elif sentence_id == 'GST':
                print('Found a GST but will not process')
            elif sentence_id == 'ZDA':
                print('Found a ZDA but will not process')
            else:
                print('Unknown GPS sentence - ' + nmea_full_sentence)
        except ValueError:
            print('[GPS-parse] Error parsing sentence')

        # Now create decimal degree values

    def parse_gga(self, nmea_full_sentence):
        # GGA - Global Positioning System Fix Data
        # $GPGGA,070700,5507.5993,N,00727.8459,W,2,09,1.23,-54.79,M,54.88,M,,*7A
        # $GNGGA,074553.00, 5507.57208, N, 00727.80468, W, 1, 12, 0.72, 6.8, M, 53.9, M,, *58
        # 1 - Fix taken at in UTC
        # 2 - Latitude (Northing)
        # 3 - NS Hemisphere
        # 4 - Longitude (Easting)
        # 5 - EW Hemisphere
        # 6 - Fix quality
        # 7 - Number of satellites being tracked
        # 8 - Horizontal dilution of position (HDOP)
        # 9 - Altitude, Metres, above mean sea level
        # 10 - Unit
        # 11 - Height of geoid (mean sea level) above WGS84 ellipsoid()
        # 12 - Unit
        # 13 - Time in seconds since last DGPS update, SC104
        # 14 - DGPS station ID number

        # print('[GPS-parseGGA] Parsing = ' + nmea_full_sentence)
        list_of_values = nmea_full_sentence.split(',')
        try:
            if list_of_values[1] == '':
                print('[GPS-parseGGA] No data')
                self.MeasurementValid = False
            else:
                # Check the fix quality
                fix_quality = list_of_values[6]
                self.quality_indicator(fix_quality)

                # If its a valid measurement, process
                if self.MeasurementValid:
                    self.GPSTime = list_of_values[1]
                    self.LatitudeDM = (list_of_values[2])
                    self.NSHemisphere = list_of_values[3]
                    self.LongitudeDM = (list_of_values[4])
                    self.EWHemisphere = list_of_values[5]
                    self.NumberOfSatellitesBeingTracked = list_of_values[7]
                    self.HDOP = list_of_values[8]
                    self.Altitude = list_of_values[9]
                    self.HeightOfGeoid = list_of_values[10]
                    self.convert_dm_to_dd()
        except ValueError:
            print('[GPS-parseGLL] Error parsing GLL')

    def parse_gll(self, nmea_full_sentence):
        # GLL - Geographic position, Latitude and Longitude
        # $GPGLL,5510.00385,N,00726.10286,W,100126.00,A,A*7E
        # $GNGLL, 5507.32671, N, 00728.16065, W, 070853.00, A, A * 63
        # 1 - Latitude (Northing)
        # 2 - NS Hemisphere
        # 3 - Longitude (Easting)
        # 4 - EW Hemisphere
        # 5 - Fix taken at in UTC
        # 6 - Data validity, A=Valid, V=Invalid
        # 7 - FAA Mode Indicator

        # print('[GPS-parseGLL] Parsing = ' + nmea_full_sentence)
        list_of_values = nmea_full_sentence.split(',')
        try:
            if list_of_values[1] == '':
                print('[GPS-parseGLL] No data')
                self.MeasurementValid = False
            else:
                # Check if fix obtained
                if list_of_values[6] == 'A':
                    self.NewMeasurement = True
                    self.MeasurementValid = True
                    self.LatitudeDM = list_of_values[1]
                    self.NSHemisphere = list_of_values[2]
                    self.LongitudeDM = list_of_values[3]
                    self.EWHemisphere = list_of_values[4]
                    self.GPSTime = list_of_values[5]
                    self.convert_dm_to_dd()
                # Check if fix lost
                elif list_of_values[6] == 'V':
                    self.MeasurementValid = False
        except ValueError:
            print('[GPS-parseGLL] Error parsing GLL')

    def parse_rmc(self, nmea_full_sentence):
        # RMC - Recommended minimum specific GPS/Transit data
        # $GPRMC,155217.00,A,5507.53477,N,00728.12803,W,3.740,246.25,151117,,,D*79
        # 1 - Fix taken at in UTC
        # 2 - Data validity, A=Valid, V=Invalid
        # 3 - Latitude (Northing)
        # 4 - NS Hemisphere
        # 5 - Longitude (Easting)
        # 6 - EW Hemisphere
        # 7 - Speed over ground, Knots
        # 8 - Course Made Good, True
        # 9 - Date of fix
        # 10 - Magnetic variation
        # 11 - Magnetic variation hemisphere

        # print('[GPS=parseRMC] Parsing = ' + nmeafullsentence)
        list_of_values = nmea_full_sentence.split(',')
        try:
            if list_of_values[1] == '':
                print('[GPS=parseRMC] No data')
                self.MeasurementValid = False
            else:
                # Check if fix obtained
                if list_of_values[2] == 'A':
                    self.NewMeasurement = True
                    self.MeasurementValid = True
                    self.LatitudeDM = (list_of_values[3])
                    self.NSHemisphere = list_of_values[4]
                    self.LongitudeDM = (list_of_values[5])
                    self.EWHemisphere = list_of_values[6]
                    self.GroundSpeedKnots = list_of_values[7]
                    self.TrackMadeGoodTrue = list_of_values[8]
                    self.GPSDate = list_of_values[9]
                    self.MagneticVariation = list_of_values[10]
                    self.MagneticVariationHemisphere = list_of_values[11]
                    self.GPSTime = list_of_values[1]
                    self.convert_dm_to_dd()
                # Check if fix lost
                elif list_of_values[2] == 'V':
                    self.MeasurementValid = False
        except ValueError:
            print('[GPS-parseRMC] Error parsing RMC')

    def parse_gsv(self, nmea_full_sentence):
        # GSV - Satellites in view
        # $GPGSV, 3, 3, 11, 29, 42, 181, 36, 31, 37, 297, 49, 32, 08, 296, 30 * 49
        # Number of sentences for full data
        # Sentence X of Y
        # Number of satellites in view
        # Satellite PRN number
        # Elevation, degrees
        # Azimuth, degrees
        # Signal(strength - higher Is better)
        # Repeat for up to 4 satellites per sentence, up to three GSV sentences in a data packet

        # Uncomment for diagnostics
        # print '[GPS=parseGSV] Parsing = ' + nmea_full_sentence
        list_of_values = nmea_full_sentence.split(',')
        try:
            if list_of_values[1] == '':
                self.MeasurementValid = False
                print('[GPS=parseGSV] No data')
            else:
                self.NumberOfSatellitesInView = list_of_values[3]

        except ValueError:
            print('[GPS-parseGSV] Error parsing')

    def parse_gsa(self, nmea_full_sentence):
        # GSA - GPS DOP and active satellites
        # $GPGSA, A, 3, 25, 12, 14, 24, 29, 31, 06, 02, 32, 03,, , 1.52, 0.83, 1.27 * 03
        # 1- Auto selection of 2D or 3D fix (A = Auto, M = manual)
        # 2- 3D fix
        # 3 - 14 PRNs of satellites used for fix (12)
        # 15 - Dilution of precision (PDOP)
        # 16 - Horizontal dilution of precision (HDOP)
        # 17 - Vertical dilution of precision (VDOP)

        # print('[GPS=parseGSA] Parsing = ' + nmea_full_sentence)
        list_of_values = nmea_full_sentence.split(',')
        try:
            if list_of_values[1] == '':
                print('[GPS=parseGSA] No data')
            else:
                self.PDOP = list_of_values[15]
                self.HDOP = list_of_values[16]
                self.VDOP = list_of_values[17]
        except ValueError:
            print('[GPS-parseGSA] Error parsing' + nmea_full_sentence)

    def parse_vtg(self, nmea_full_sentence):
        # VTG - Track made good and ground speed
        # $GPVTG,246.25,T,,M,3.740,N,6.927,K,D*35
        # 1 - True track made good
        # 3 - Magnetic track made good
        # 3 - Ground speed, knots
        # 4 - Ground speed, Kilometers per hour

        # Uncomment for diagnostics
        # print ('[GPS=parseVTG] Parsing = ' + nmea_full_sentence)
        list_of_values = nmea_full_sentence.split(',')
        try:
            if list_of_values[1] != '':
                self.TrackMadeGoodTrue = float(list_of_values[1])
            if list_of_values[3] != '':
                self.TrackMadeGoodMagnetic = float(list_of_values[3])
            if list_of_values[5] != '':
                self.GroundSpeedKnots = float(list_of_values[5])
            if list_of_values[7] != '':
                self.GroundSpeedKMH = float(list_of_values[7])
        except ValueError:
            print('[GPS-parseVTG] Error parsing ' + nmea_full_sentence)

    def convert_dm_to_dd(self):
        # Position in the format 5507.6866 converts to 55.166755
        dm_latitude_degrees = int(self.LatitudeDM[0:2])
        dm_latitude_minutes = float(self.LatitudeDM[2:])
        dm_latitude_minutes_fraction = float(dm_latitude_minutes / 60)
        self.LatitudeDD = round(dm_latitude_degrees + dm_latitude_minutes_fraction, 7)
        # Position in the format 00728.2919 converts to 7.166755
        dm_longitude_degrees = int(self.LongitudeDM[0:3])
        dm_longitude_minutes = float(self.LongitudeDM[3:])
        dm_longitude_minutes_fraction = float(dm_longitude_minutes / 60)
        self.LongitudeDD = round(-dm_longitude_degrees - dm_longitude_minutes_fraction, 7)

    def quality_indicator(self, value):
        if value == '0':
            self.FixType = 'No fix'
            self.NewMeasurement = False
            self.MeasurementValid = False
        elif value == '1':
            self.FixType = 'GPS Fix'
            self.NewMeasurement = True
            self.MeasurementValid = True
        elif value == '2':
            self.FixType = 'DGPS Fix'
            self.NewMeasurement = True
            self.MeasurementValid = True
        elif value == '3':
            self.FixType = 'PPS Fix'
            self.NewMeasurement = True
            self.MeasurementValid = True
        elif value == '4':
            self.FixType = 'RTK Fix'
            self.NewMeasurement = True
            self.MeasurementValid = True
        elif value == '5':
            self.FixType = 'RTK Float Fix'
            self.NewMeasurement = True
            self.MeasurementValid = True
        elif value == '6':
            self.FixType = 'Estimated'
            self.NewMeasurement = False
            self.MeasurementValid = False
        elif value == '7':
            self.FixType = 'Manual'
            self.NewMeasurement = False
            self.MeasurementValid = False
        elif value == '8':
            self.FixType = 'Simulation'
            self.NewMeasurement = False
            self.MeasurementValid = False
        else:
            return 'Error'

    @staticmethod
    def faa_mode_indicator(value):
        if value == 'A':
            return 'Autonomous'
        elif value == 'D':
            return 'Differential'
        elif value == 'E':
            return 'Estimated'
        elif value == 'M':
            return 'Manual'
        elif value == 'S':
            return 'Simulator'
        elif value == 'N':
            return 'Invalid'
        else:
            return 'Error'
















