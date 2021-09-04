
import json
from pathlib import Path
from random import randint
import yaml

#data_path = Path("models","building","data")
data_path = Path()


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


def read_building_data_yaml(userID, filepath = data_path):
    """Read the building parameters from a yaml file.

    Parameters
    ----------
    buildingID : str
        ID of the building
    filepath : pathlib Path
        filepath where the yaml file is saved
    """

    filename = Path(filepath , userID + "_building.yaml")
    with open (filename) as f:
        data = yaml.load(f, Loader = yaml.FullLoader)
    return data

def save_building_data_yaml(building, filepath = data_path):
    """Save the building parameters in a yaml file.

    Parameters
    ----------
    building : dict
        dictionary with building parameters
    filepath : pathlib Path
        filepath where the yaml file should be saved
    """

    filename = Path(filepath , str(building["id"]) + "_building.yaml")
    with open(filename, 'w') as f:
        yaml.dump(building, f)

'''
building = {
    "id": randint(0,1e9),
    "location": {
        "latitude": None,       # Latitude [decimal degrees]
        "longitude": None,      # Longitude [decimal degrees]
        },
    "weatherFile": None,        # Filename of the weather file [string]
    "groundArea": XX,           # Ground area in [m^2]
    "n_storys" : XX,            # number of storys
    "thZones" : {
        "livingSpace" : {
            "volume" : None,    # Volume [m^3]
            "floorArea" : None, # Floor area of thermal zone [m^2]
            "heated" : True,    
            "tempIn" : None,    # Indoor temperature [°C]
            "gainsInt" : None,  # Internal gains [W/m^2]
            "nInf" : None,      # Infiltration number [1/h]
            "nVent" : None,     # Ventilation number [1/h]
            "opaquePlanes" : {  # Walls, Ceiling/Floor, Roof
                "facade": {
                    "adjTZ" : "ambient",  # adjacent thermal zone (string) i.e. ambient, ground, tzX
                    "u-value": None, # U-value [W/m^2/K]
                    "area" : None,   # area of the plane [m^2] 
                },
                "ceiling": {
                    "adjTZ" : "attic",  # adjacent thermal zone (string) i.e. ambient, ground, tzX
                    "u-value": None, # U-value [W/m^2/K]
                    "area" : None,   # area of the plane [m^2] 
                },
                "floor": {
                    "adjTZ" : "basement",  # adjacent thermal zone (string) i.e. ambient, ground, tzX
                    "u-value": None, # U-value [W/m^2/K]
                    "area" : None,   # area of the plane [m^2] 
                },
            },
            "transPlanes" : { # transparent planes e.g. windows, transparent doors
                "windowA" : {
                    "adjTZ" : None,  # adjacent thermal zone (string) i.e. ambient, ground, tzX
                    "u-value": None, # U-value [W/m^2/K]
                    "area" : None,   # area of the plane [m^2] 
                    "g-value" : None, # solar heat gain coefficient [-]
                    "tilt" : None,    # tilt angle [deg]
                    "azimuth": None,  # azimuth angle 0 = north, 90 = east ... [deg]
                }
                "windowB" : {
                    "adjTZ" : None,  # adjacent thermal zone (string) i.e. ambient, ground, tzX
                    "u-value": None, # U-value [W/m^2/K]
                    "area" : None,   # area of the plane [m^2] 
                    "g-value" : None, # solar heat gain coefficient [-]
                    "tilt" : None,    # tilt angle [deg]
                    "azimuth": None,  # azimuth angle 0 = north, 90 = east ... [deg]
                }
                "windowC" : {
                    "adjTZ" : None,  # adjacent thermal zone (string) i.e. ambient, ground, tzX
                    "u-value": None, # U-value [W/m^2/K]
                    "area" : None,   # area of the plane [m^2] 
                    "g-value" : None, # solar heat gain coefficient [-]
                    "tilt" : None,    # tilt angle [deg]
                    "azimuth": None,  # azimuth angle 0 = north, 90 = east ... [deg]
                }
                "windowD" : {
                    "adjTZ" : None,  # adjacent thermal zone (string) i.e. ambient, ground, tzX
                    "u-value": None, # U-value [W/m^2/K]
                    "area" : None,   # area of the plane [m^2] 
                    "g-value" : None, # solar heat gain coefficient [-]
                    "tilt" : None,    # tilt angle [deg]
                    "azimuth": None,  # azimuth angle 0 = north, 90 = east ... [deg]
                }
            }    
        },
        "attic" : {
            "volume" : None,    # Volume [m^3]
            "floorArea" : None, # Floor area of thermal zone [m^2]
            "heated" : False,
            "tempIn" : None,    # Indoor temperature [°C]
            "gainsInt" : None,  # Internal gains [W/m^2]
            "nInf" : None,      # Infiltration number [1/h]
            "nVent" : None,     # Ventilation number [1/h]
            "opaquePlanes" : {  # Walls, Ceiling/Floor, Roof
                "roof": {
                    "adjTZ" : "ambient",  # adjacent thermal zone (string) i.e. ambient, ground, tzX
                    "u-value": None, # U-value [W/m^2/K]
                    "area" : None,   # area of the plane [m^2] 
                },
                "floor": {
                    "adjTZ" : "livingSpace",  # adjacent thermal zone (string) i.e. ambient, ground, tzX
                    "u-value": None, # U-value [W/m^2/K]
                    "area" : None,   # area of the plane [m^2] 
                },
            },
            "transPlanes" : { # transparent planes e.g. windows, transparent doors
                "windowA" : {
                    "adjTZ" : None,  # adjacent thermal zone (string) i.e. ambient, ground, tzX
                    "u-value": None, # U-value [W/m^2/K]
                    "area" : None,   # area of the plane [m^2] 
                    "g-value" : None, # solar heat gain coefficient [-]
                    "tilt" : None,    # tilt angle [deg]
                    "azimuth": None,  # azimuth angle 0 = north, 90 = east ... [deg]
                }
                "windowB" : {
                    "adjTZ" : None,  # adjacent thermal zone (string) i.e. ambient, ground, tzX
                    "u-value": None, # U-value [W/m^2/K]
                    "area" : None,   # area of the plane [m^2] 
                    "g-value" : None, # solar heat gain coefficient [-]
                    "tilt" : None,    # tilt angle [deg]
                    "azimuth": None,  # azimuth angle 0 = north, 90 = east ... [deg]
                }
            }    
        },
        "basement" : {
            "volume" : None,    # Volume [m^3]
            "floorArea" : None, # Floor area of thermal zone [m^2]
            "heated" : False,
            "tempIn" : None,    # Indoor temperature [°C]
            "gainsInt" : None,  # Internal gains [W/m^2]
            "nInf" : None,      # Infiltration number [1/h]
            "nVent" : None,     # Ventilation number [1/h]
            "opaquePlanes" : {  # Walls, Ceiling/Floor, Roof
                "ceiling": {
                    "adjTZ" : "livingSpace",  # adjacent thermal zone (string) i.e. ambient, ground, tzX
                    "u-value": None, # U-value [W/m^2/K]
                    "area" : None,   # area of the plane [m^2] 
                },
                "ground": {
                    "adjTZ" : "ground",  # adjacent thermal zone (string) i.e. ambient, ground, tzX
                    "u-value": None, # U-value [W/m^2/K]
                    "area" : None,   # area of the plane [m^2] 
                },
            },
            "transPlanes" : { # transparent planes e.g. windows, transparent doors
                "windowA" : {
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

