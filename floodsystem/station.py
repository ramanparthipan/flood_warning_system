# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    def typical_range_consistent(self):
        "This method checks the consistency of station data with typical high/low values"
        if self.typical_range == None:
            return False 
        temp = self.typical_range
        math_range = float(temp[1])-float(temp[0])
        if math_range < 0 or not self.typical_range:
            return False
        else:
            return True

    def inconsistent_typical_range_stations(stations):
        inconsistent_stations = []
        for station in stations:
            if type(station.typical_range) == type([].sort()):
                inconsistent_stations.append(station)
            else:
                if not MonitoringStation.typical_range_consistent(station):
                    inconsistent_stations.append(station)
                else:
                    pass
        return inconsistent_stations
    
    """def relative_water_level(self):
        if self.latest_level == None or self.typical_range_consistent == False:
                return None
        else:
            return(self.latest_level - self.typical_range[0])/(self.typical_range[1]-self.typical_range[0])"""
    
    def relative_water_level(self):

        '''Takes in self (station object)
        Returns a value from 0.0 to 1.0 describing the latest relative water level
        Returns None when data is out of range or inconsistent
        '''

        if (not self.typical_range_consistent()) or (self.latest_level==None):
            return None
        return (self.latest_level-self.typical_range[0])/(self.typical_range[1]-self.typical_range[0])
    



