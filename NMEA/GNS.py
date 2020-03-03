from NMEA.Utilities import quality_indicator, faa_mode_indicator, convert_dm_to_dd


class GNS_Talker:

    def __init__(self, talker_id):  # Init for instances
        self.talker_id = talker_id
        self.NewMeasurement = False
        self.MeasurementValid = False
        self.Latitude = ''
        self.Longitude = ''

    def parse_gns(self, sentence):

        # GNS - GNSS fix data
        # $GNGNS,150233.00,5510.00879,N,00726.10787,W,FF,19,0.66,111.2,53.9,1.0,0000*5A
        # $GNGNS,145146.00,5510.01172,N,00726.09453,W,AA,18,0.64,109.5,53.9,,*7C
        # $GNGNS, 082636.00, 5507.55102, N, 00727.92759,W,RR,14,0.77,0.8,53.9,1.0,0000*58
        # 1 - Fix taken at time in UTC
        # 2 - Latitude (Northing)
        # 3 - NS Hemisphere
        # 4 - Longitude (Easting)
        # 5 - EW Hemisphere
        # 6 - Position Mode, GPS, GLONASS, Galileo, BeiDou (N, E, F, R, A/D)
        # 7 - Number of satellites being tracked
        # 8 - Horizontal dilution of position (HDOP)
        # 9 - Altitude, Meters, above mean sea level
        # 10 - Unit
        # 11 - Height of geoid (mean sea level) above ETRS89 ellipsoid
        # 12 - Unit
        # 13 - Time in seconds since last DGPS update, SC104
        # 14 - DGPS station ID number

        # print('[GPS-parseGNS] Parsing = ' + sentence)
        list_of_values = sentence.split(',')
        try:
            if list_of_values[1] == '':
                print('[Parse GNS] No data')
                measurement_valid = False
            else:
                # Check the fix quality
                #fix_quality = list_of_values[6]
                #quality_indicator(fix_quality)
                self.MeasurementValid = True

                # If its a valid measurement, process
                if self.MeasurementValid:
                    _GPSTime = list_of_values[1]
                    _LatitudeDM = (list_of_values[2])
                    _NSHemisphere = list_of_values[3]
                    _LongitudeDM = (list_of_values[4])
                    _EWHemisphere = list_of_values[5]
                    _NumberOfSatellitesBeingTracked = list_of_values[7]
                    _HDOP = list_of_values[8]
                    _Altitude = list_of_values[9]
                    _HeightOfGeoid = list_of_values[10]
                    self.Latitude, self.Longitude = convert_dm_to_dd(_LatitudeDM, _LongitudeDM)

        except ValueError:
            print('[GPS-parseGLL] Error parsing GLL')