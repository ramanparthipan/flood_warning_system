from floodsystem.utils import sorted_by_key


def stations_level_over_threshold(stations, tol):
    """ this returns a list of tuples where the relative water level is over tol"""
    over_threshold_list = []
    for s in stations:
        rwl = s.relative_water_level()
        if rwl is not None and rwl > tol:
            over_threshold_list.append((s, rwl))
    return sorted_by_key(over_threshold_list, 1, reverse=True)

def stations_highest_rel_level(stations, N):
    """ this returns a list of tuples N where the relative water level is highest"""
    water_level_relative = []
    # initialise empty list
    for station in stations:
        if station.relative_water_level() == None:
             # If the water level is set to null(no data), don't add it to the list
            pass
        else:
            water_level_relative.append((station, station.relative_water_level())) 
            # add it to the list
    SortedList = sorted_by_key(water_level_relative, 1, reverse=True)
    # For descending order

    a = SortedList[:N]
    b = []
    for X in a:
        b.append(X[0])
    return b