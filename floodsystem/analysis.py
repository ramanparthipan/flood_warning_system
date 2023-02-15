import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from floodsystem.stationdata import build_station_list
from datetime import datetime, timedelta


def polyfit(dates, levels, p):
    """Given a list of floats 'dates' (where each number represents the number of 
    days of a date from a fixed date), a list of integers 'levels' and 
    a polynomial order 'p', this function returns the tuple 
    poly, d0
    where poly is a numpy.poly1d object representing the polynomial line of best fit of the data
    and d0 is the shift of the fixed date the dates are measured from. """
    # Find coefficients of best-fit polynomial f(x) of degree p
    d0 = dates[-1] - 1
    datesshifted = dates - d0
    
    p_coeff = np.polyfit(datesshifted, levels, p)

    # Convert coefficient into a polynomial that can be evaluated,
    poly = np.poly1d(p_coeff)

    return poly, d0









