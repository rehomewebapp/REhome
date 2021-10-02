from app import app
from dash.dependencies import Input, Output

import pandas as pd
import datetime

from models.building import physics
from models.building.buildingFactory import read_building_data_yaml
from models.building.utilities import read_tmy_data
from views.templates.graphs import create_bar_graph


def prepare_graph():

    # read building facade area
    building = read_building_data_yaml(userID='userID')
    facadeArea = building['thZones']['livingSpace']['opaquePlanes']['facade']['area']
    roofArea = building['thZones']['livingSpace']['opaquePlanes']['roof']['area']
    floorArea = building['thZones']['livingSpace']['opaquePlanes']['floor']['area']
    u_facade = building['thZones']['livingSpace']['opaquePlanes']['facade']['uValue']
    u_roof = building['thZones']['livingSpace']['opaquePlanes']['roof']['uValue']
    u_floor = building['thZones']['livingSpace']['opaquePlanes']['floor']['uValue']
    #load weather data
    index = pd.date_range(datetime.datetime(2021,1,1), periods=8760, freq="h")
    #data = read_tmy_data("userID")
    tempAmb = read_tmy_data("userID")['T2m']
    tempAmb.index = index
    
    #load comfort temp
    temp_comfort=building['thZones']['livingSpace']['tempIn']

    #TO DO: find good model for ground temperature
    #tempGround = 12
    tempGround = tempAmb * 0.5

    #temperature = data['T2m']
    df = pd.DataFrame(index = index)
    df['Qflow_trans_facade'] = physics.transmission(u_facade, facadeArea, temp_comfort, tempAmb)
    df['Qflow_trans_roof'] = physics.transmission(u_roof, roofArea, temp_comfort, tempAmb)
    df['Qflow_trans_ground'] = physics.transmission(u_floor, floorArea, temp_comfort, tempGround)
    
    df['Qflow_int'] = physics.internalGains(area = building['thZones']['livingSpace']['floorArea'], 
                                           specInternalGains= building['thZones']['livingSpace']['gainsInt'])

    df['Qflow_vent'] = physics.infAndVent(n = building['thZones']['livingSpace']['nVent'] + building['thZones']['livingSpace']['nInf'],
                                        volume = building['thZones']['livingSpace']['volume'],
                                        tempIn = temp_comfort,
                                        tempAmb = tempAmb)

    graph = create_bar_graph(df)
    return graph


@app.callback(
    Output('heatDemand_content_id', 'children'),
    Input("update_graphs_button_id", "n_clicks"),
)
#def inputDone(location_clicks, occupancy_clicks, floorplan_clicks, geometry_clicks, materials_clicks):
def inputDone(n_clicks):
    graph = prepare_graph()
    return graph