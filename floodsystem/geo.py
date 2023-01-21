# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit
from .stationdata import build_station_list # don't need except to test functions


def stations_by_distance(stations, p):
    """Given a list of stations and a coordinate p, returns a list of tuples containing the station name
    and its distance to p, sorted in increasing order of distance. """
    distances = []
    for station in stations:
        distances.append((station, haversine(p, station.coord))) #distance in km
    return sorted_by_key(distances, 1)



if __name__ == "__main__":
    stations = build_station_list()
    print(stations_by_distance(stations[:3], (52.2053, 0.1218)))






