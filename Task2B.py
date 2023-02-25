from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels


def run():
    """Demonstration task for 2B"""
    # builds and updates a list of stations
    stations = build_station_list()
    update_water_levels(stations)
    # gets all stations with a relative water level of 0.8 or more and displays it
    over_threshold = stations_level_over_threshold(stations, 0.8)
    for s, rwl in over_threshold:
        print(s.name, rwl)

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()


