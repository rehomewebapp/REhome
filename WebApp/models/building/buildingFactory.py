
import json
from pathlib import Path
from random import randint

#data_path = Path("models","building","data")
data_path = Path()

def createBuilding():
    building = {
    #"id": randint(0,1e9),
    "id" : "userID",
    'thZones' : {'tz0':{'opaquePlanes':{'roof':{},'facade':{},'floor':{}}}}
    }
    return building


def save_building_data(building, filepath = data_path):
    """Save the building parameters in a json file.

    Parameters
    ----------
    building : dict
        dictionary with building parameters
    filepath : pathlib Path
        filepath where the json file should be saved
    """

    filename = Path(filepath , str(building["id"]) + "_building.json")
    with open(filename, 'w') as f:
        json.dump(building, f)

def read_building_data(userID, filepath = data_path):
    """Read the building parameters from a json file.

    Parameters
    ----------
    buildingID : str
        ID of the building
    filepath : pathlib Path
        filepath where the json file is saved
    """

    filename = Path(filepath , userID + "_building.json")
    with open(filename, 'r') as f:
        data = f.read()
    building = json.loads(data)

    return building


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
            "heatedArea" : None, # Heated living area [m^2]
            "perimeter" : None, # Perimeter of the floor area in [m]
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