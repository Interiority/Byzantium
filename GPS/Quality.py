import statistics


class GNSQuality:
    def __init__(self):        # Init for instances
        self.Latitudes = []
        self.Longitudes = []
        self.latitude_tolerance = .00000001
        self.longitude_tolerance = .00000001

        self.latitude_median_error = False
        self.longitude_median_error = False

        self.last_latitude = 55.1
        self.last_longitude = 7.2
        self.last_second = 180401

    def run(self):
        self.find_median()

    def add_values(self, longitude, latitude):
        self.last_longitude = longitude
        self.last_latitude = latitude

        self.Latitudes.append(latitude)
        self.Longitudes.append(longitude)

    def find_median(self):
        if len(self.Latitudes) > 5:
            latitude_median = statistics.median(self.Latitudes)
            upper_limit = latitude_median + self.latitude_tolerance
            lower_limit = latitude_median - self.latitude_tolerance

            if self.last_latitude > upper_limit:
                self.latitude_median_error = True
                print('MEDIAN: {} is greater than {}'.format(self.last_latitude, upper_limit))
            else:
                self.latitude_median_error = False
                #print('{} is not greater than {}'.format(self.last_latitude, upper_limit))

            if self.last_latitude < lower_limit:
                self.latitude_median_error = True
                print('MEDIAN: {} is less than {}'.format(self.last_latitude, lower_limit))
            else:
                self.latitude_median_error = False
                #print('{} is not less than {}'.format(self.last_latitude, lower_limit))

        if len(self.Longitudes) > 5:
            longitude_median = statistics.median(self.Longitudes)
            upper_limit = longitude_median + self.longitude_tolerance
            lower_limit = longitude_median - self.longitude_tolerance

            if self.last_longitude > upper_limit:
                self.longitude_median_error = True
                print('MEDIAN: {} is greater than {}'.format(self.last_longitude, upper_limit))
            else:
                self.longitude_median_error = False
                #print('{} is not greater than {}'.format(self.last_longitude, upper_limit))

            if self.last_longitude < lower_limit:
                self.longitude_median_error = True
                print('MEDIAN: {} is less than {}'.format(self.last_longitude, lower_limit))
            else:
                self.longitude_median_error = False
                #print('{} is not less than {}'.format(self.last_longitude, lower_limit))



