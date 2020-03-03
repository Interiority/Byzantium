
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


def faa_mode_indicator(value):
    if value == 'A':
        return 'Autonomous'
    elif value == 'F':
        return 'RTKFloat'
    elif value == 'R':
        return 'RTKFixed'
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


def convert_dm_to_dd(LatitudeDM, LongitudeDM):
    # Position in the format 5507.6866 converts to 55.166755
    dm_latitude_degrees = int(LatitudeDM[0:2])
    dm_latitude_minutes = float(LatitudeDM[2:])
    dm_latitude_minutes_fraction = float(dm_latitude_minutes / 60)
    LatitudeDD = round(dm_latitude_degrees + dm_latitude_minutes_fraction, 10)

    # Position in the format 00728.2919 converts to 7.166755
    dm_longitude_degrees = int(LongitudeDM[0:3])
    dm_longitude_minutes = float(LongitudeDM[3:])
    dm_longitude_minutes_fraction = float(dm_longitude_minutes / 60)
    LongitudeDD = round(-dm_longitude_degrees - dm_longitude_minutes_fraction, 10)

    return LatitudeDD, LongitudeDD
