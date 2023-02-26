from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.analysis import polyfit # polynomial fit to data
from datetime import datetime, timedelta
from floodsystem.datafetcher import fetch_measure_levels
import matplotlib
from floodsystem.geo import stations_within_radius

def run():
    """Requirements for 2G""" #Describe the methodology here
    stations = build_station_list()
    update_water_levels(stations)
    over_threshold = stations_level_over_threshold(stations, 1.0) # stations with water level above their typical high
    for s, rwl in over_threshold:
        print()
        # print(s.name, rwl)
        dt = 2
        dates, levels = fetch_measure_levels(s.measure_id,
                                     dt=timedelta(days=dt))
        p = 4 # order of polynomial fit
        datesfloat = matplotlib.dates.date2num(dates) # datesfloat is a list of the number of days since the start of the
        # gregorian calender. The most recent dates (highest number of days) are first.
        poly, d0 = polyfit(datesfloat, levels, p)
        datesshifted = datesfloat - d0
        poly_deriv = poly.deriv() # gradient of polyfit
        #print(poly_deriv)
        datesshifted = datesfloat - d0 # the least recent day is set to day 1, which are the dates poly is fitted to.
        # print(poly_deriv(datesshifted[0])) # final gradient of the polynomial line of best fit.
        if poly_deriv(datesshifted[0]) > 0: # water level is predicted to rise
            print(f'Town name: {s.town}; Risk: Severe; Reason: {s.river} above normal water levels and water level is predicted to increase')
        else:
            print(f'Town name: {s.town}; Risk: High; Reason: {s.river} above normal water levels but water level is predicted to decrease')

        stations_within_radius_list = stations_within_radius(stations, s.coord, 5) # stations within 5km of risky stations
        for station in stations_within_radius_list:
            if station is not s and station.town is not None:
                print(f'Town name: {station.town}; Risk: Moderate; Reason: {station.town} is within 5km of {s.river} which has a high or severe risk of flooding')
        print()


if __name__ == "__main__":
    run()



# Find the towns with relative water level above 1.0. Calculate the gradients. If positive, put severe,
# if negative or zero, put high.
# Then find the stations within 5km of those stations and put their flood risk as moderate. Put the
# other stations as low.

