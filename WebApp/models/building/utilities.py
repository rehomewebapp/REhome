import requests
import json
import pandas as pd
from pathlib import Path

#data_path = Path("models","building","data")
data_path = Path()

def get_tmy_data(latitude, longitude):
    """Load weather - typical meterological year(TMY) data from PVGIS

    Parameters
    ----------
    latitude : float
        Latitude [decimal degrees]
    longitude : float
        Longitude [decimal degrees]

    Returns
    -------
    pandas df containing

        - time (index, datetime): Date & time (UTC)
        - T2m (pandas column, float): Dry bulb (air) temperature [°C]
        - RH (pandas column, float):  Relative Humidity [%]
        - G(h) (pandas column, float): Global horizontal irradiance [W/m2]
        - Gb(n) (pandas column, float): Direct (beam) irradiance [W/m2]
        - Gd(h) (pandas column, float): Diffuse horizontal irradiance [W/m2]
        - IR(h) (pandas column, float): Infrared radiation downwards [W/m2]
        - WS10m (pandas column, float): Windspeed [m/s]
        - WD10m (pandas column, float): Wind direction [°]
        - SP (pandas column, float): Surface (air) pressure [Pa]

    Notes
    -----
    A typical meteorological year (TMY) is a set of meteorological data with data values 
    for every hour in a year for a given geographical location. The data are selected from hourly 
    data in a longer time period (normally 10 years or more). 
    The TMY is generated in PVGIS following the procedure described in ISO 15927-4. [1]_

    References
    ----------

    .. [1] https://ec.europa.eu/jrc/en/PVGIS/tools/tmy

    """

    url = 'https://re.jrc.ec.europa.eu/api/tmy?lat='+str(latitude)+'&lon='+str(longitude)+'&outputformat=json'
    
    response = requests.get(url)
    data = json.loads(response.text)
    data_outputs_hourly = data['outputs']['tmy_hourly']
    df = pd.DataFrame.from_dict(data_outputs_hourly)
    df.set_index('time(UTC)', inplace = True)
    df.index = pd.to_datetime(df.index, format = '%Y%m%d:%H%M')
    return df

def save_tmy_data(df, userID = "userID", filepath = data_path):
    """Save the weather data in a json file.

        Parameters
        ----------
        df : pandas dataframe
            dataframe containing weather data
        userID : str
            ID of the user
        filepath : pathlib Path
            filepath where the json file should be saved
    """
    
    weatherData = df.to_json()
    filename = filepath + userID + "_weather.json"
    with open(filename, 'w') as f:
        json.dump(weatherData, f)

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

#save_building_data(building, "models/building/data/")


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

def save_location_data(location, filepath = data_path, userID = "userID"):
    """Save the location in the building's json file.

        Parameters
        ----------
        userID : str
            ID of the building
        location : list of float
            latitude, longitude [decimal degrees]
        filepath : pathlib Path
            filepath where the json file is saved
    """
    lat = location[0]
    long = location[1]
    building = read_building_data(userID, filepath)
    building["location"] = {
        "latitude": lat,       # Latitude [decimal degrees]
        "longitude": long,     # Longitude [decimal degrees]
    }
    save_building_data(building, filepath)



#building1 = read_building_data("335662254", "models/building/data/")
#pprint.pprint(building1)


''' example for creating a wall
wall = {
    "adjTZ" : "ambient",  # adjacent thermal zone (string) i.e. ambient, ground, tzX
    "u-value": 2, # U-value [W/m^2/K]
    "area" : 20,   # area of the plane [m^2] 
}

opaquePlanes = building.thZones.tz0.opaquePlanes

opaquePlanes["op1"] = wall
'''





if __name__ == "__main__":
    df = get_tmy_data(48,8)
    print(df)
