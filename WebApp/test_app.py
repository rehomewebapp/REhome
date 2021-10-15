# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 10:31:02 2021

@author: Lukas
"""

import pandas as pd
import datetime
import pvlib

from models.building import physics
from models.building.buildingFactory import read_building_data_yaml
from models.building.utilities import read_tmy_data
from views.templates.graphs import create_bar_graph




building = read_building_data_yaml(userID='userID')
facadeArea = building['thZones']['livingSpace']['opaquePlanes']['facade']['area']
roofArea = building['thZones']['livingSpace']['opaquePlanes']['roof']['area']
floorArea = building['thZones']['livingSpace']['opaquePlanes']['floor']['area']
u_facade = building['thZones']['livingSpace']['opaquePlanes']['facade']['uValue']
u_roof = building['thZones']['livingSpace']['opaquePlanes']['roof']['uValue']
u_floor = building['thZones']['livingSpace']['opaquePlanes']['floor']['uValue']
latitude = building['location']['latitude']
longitude = building['location']['longitude']


#load weather data
index = pd.date_range(datetime.datetime(2021,1,1), periods=8760, freq="h")
#data = read_tmy_data("userID")
weatherdata = read_tmy_data("userID")
tempAmb = weatherdata['T2m']
weatherdata.index = index

#load comfort temp
temp_comfort=building['thZones']['livingSpace']['tempIn']

#TO DO: find good model for ground temperature
#tempGround = 12
tempGround = tempAmb * 0.5

#calculate solar irradiance on windows
location = pvlib.location.Location(latitude = latitude,
                                    longitude = longitude,
                                    tz = 'Europe/Berlin', # !TODO get timezone from location
                                    )       

solarposition = location.get_solarposition(times = index)


# handle window heat flows
q_flow_trans_window, q_flow_sol_window = 0, 0
for window in building['thZones']['livingSpace']['transPlanes']:
    area = building['thZones']['livingSpace']['transPlanes'][window]['area']
    u_window = building['thZones']['livingSpace']['transPlanes'][window]['uValue']
    g_window = building['thZones']['livingSpace']['transPlanes'][window]['gValue']
    tilt = building['thZones']['livingSpace']['transPlanes'][window]['tilt']
    azimuth = building['thZones']['livingSpace']['transPlanes'][window]['azimuth']
    #calculate transmission through window
    q_flow_trans_window += physics.transmission(u_window, area, temp_comfort, tempAmb)

    poa = pvlib.irradiance.get_total_irradiance(surface_tilt = tilt,
                                                surface_azimuth = azimuth,
                                                solar_zenith = solarposition.zenith,
                                                solar_azimuth = solarposition.azimuth,
                                                dni = weatherdata['Gb(n)'],
                                                ghi = weatherdata['G(h)'],
                                                dhi = weatherdata['Gd(h)'],
                                                ).poa_global.fillna(0)


    # calculate solar gains through window
    q_flow_sol_window += physics.solarGains(gValue = g_window, area = area, irrad = poa)
