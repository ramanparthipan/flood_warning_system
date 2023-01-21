from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():
    """Requirements for Task 1B. Returns the tuple of lists (closest_cambridge_stations, farthest_cambridge_stations)"""
    stations = build_station_list()
    distances = stations_by_distance(stations, (52.2053, 0.1218)) # from coordinates of Cambridge city centre
    closest_cambridge_stations = []
    for (station, distance) in distances[:10]:
        closest_cambridge_stations.append((station.name, station.town, distance))

    farthest_cambridge_stations = []
    for (station, distance) in distances[-10:]:
        farthest_cambridge_stations.append((station.name, station.town, distance))
    
    return (closest_cambridge_stations, farthest_cambridge_stations)

if __name__ == "__main__":
    (closest_cambridge_stations, farthest_cambridge_stations) = run()
    print('Closest cambridge stations: {}'.format(closest_cambridge_stations))
    print()
    print('Farthest cambridge stations: {}'.format(farthest_cambridge_stations))