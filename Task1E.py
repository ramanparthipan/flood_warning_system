from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_river
list_of_stations=build_station_list()



def run(N):
    answer=rivers_by_station_number(list_of_stations,N)
    return answer
print(run(9))


