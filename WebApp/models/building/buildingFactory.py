
import json
from random import randint

'''
building = {
    "id": randint(0,1e9),
    "location": {
        "latitude": None,       # Latitude [decimal degrees]
        "longitude": None,      # Longitude [decimal degrees]
        },
    "weatherFile": None,        # Filename of the weather file [string]
    "thZones" : {
        "tz0" : {
            "name" : None,       # e.g. kitchen, bedroom, basement
            "volume" : None,    # Volume [m^3]
            "floorArea" : None, # Floor area in [m^2]
            "tempIn" : None,    # Indoor temperature [°C]
            "gainsInt" : None,  # Internal gains [W/m^2]
            "nInf" : None,      # Infiltration number [1/h]
            "nVent" : None,     # Ventilation number [1/h]
            "opaquePlanes" : {  # Walls, Ceiling/Floor, Roof
                "op0": {
                    "adjTZ" : None,  # adjacent thermal zone (string) i.e. ambient, ground, tzX
                    "u-value": None, # U-value [W/m^2/K]
                    "area" : None,   # area of the plane [m^2] 
                },
            },
            "transPlanes" : { # transparent planes e.g. windows, transparent doors
                "tp0" : {
                    "adjTZ" : None,  # adjacent thermal zone (string) i.e. ambient, ground, tzX
                    "u-value": None, # U-value [W/m^2/K]
                    "area" : None,   # area of the plane [m^2] 
                    "g-value" : None, # solar heat gain coefficient [-]
                    "tilt" : None,    # tilt angle [deg]
                    "azimuth": None,  # azimuth angle 0 = north, 90 = east ... [deg]
                }
            }    
        }
    }
}
'''

def createBuilding():
    building = {
    #"id": randint(0,1e9),
    "id" : "userID"
    }
    return building
