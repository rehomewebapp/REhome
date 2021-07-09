
import json
from random import randint
import pprint

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

def save_building_data(building, filepath):

    """Save the building parameters in a json file.

        Parameters
        ----------
        building : dict
            dictionary with building parameters
        filepath : str
            filepath where the json file should be saved
    """

    filename = filepath + str(building["id"]) + ".json"
    with open(filename, 'w') as f:
        json.dump(building, f)

#save_building_data(building, "models/building/data/")


def read_building_data(buildingID, filepath):
    """Read the building parameters from a json file.

        Parameters
        ----------
        buildingID : str
            ID of the building
        filepath : str
            filepath where the json file is saved
    """

    filename = filepath + buildingID + ".json"
    with open(filename, 'r') as f:
        data = f.read()
    building = json.loads(data)

    return building

building1 = read_building_data("335662254", "models/building/data/")
pprint.pprint(building1)


''' example for creating a wall
wall = {
    "adjTZ" : "ambient",  # adjacent thermal zone (string) i.e. ambient, ground, tzX
    "u-value": 2, # U-value [W/m^2/K]
    "area" : 20,   # area of the plane [m^2] 
}

opaquePlanes = building.thZones.tz0.opaquePlanes

opaquePlanes["op1"] = wall
'''