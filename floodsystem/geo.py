# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit


def stations_by_distance(stations, p):
    """Given a list of stations and a coordinate p, returns a list of tuples containing the station object
    and its distance to p, sorted in increasing order of distance. """
    distances = []
    for station in stations:
        distances.append((station, haversine(p, station.coord))) #distance in km
    return sorted_by_key(distances, 1)

def stations_within_radius(stations, centre, r):
    """Returns the list of stations within a distance r from a point."""
    distances = stations_by_distance(stations, centre)
    stations_within_radius_list = []
    for item in distances:
        if item[1] > r:
            break
        stations_within_radius_list.append(item[0])
    return stations_within_radius_list






