from app import app
from dash.dependencies import Input, Output
from dash import callback_context

import pandas as pd
import datetime

from models.building import physics
from models.building.buildingFactory import save_building_data_yaml, read_building_data_yaml
from models.building.utilities import read_tmy_data
from views.templates.graphs import create_graph


@app.callback(
    #Output("materials_output_id","children"),
    Output('materials_done_button_id', 'disabled'), 
    Output('materials_done_button_id', 'color'),
    Output("u_facade_id", "value"),
    Output("u_roof_id", "value"),
    Output("u_floor_id", "value"),
    Input("u_facade_id", "value"),
    Input("u_roof_id", "value"),
    Input("u_floor_id", "value"),
    Input("materials_done_button_id", "n_clicks")
)
def inputDone(u_facade, u_roof, u_floor, n_clicks):

    ctx = callback_context
    # check which input has triggered the callback
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    # on pageload: fill input fields with building data
    if not ctx.triggered:
        building = read_building_data_yaml("userID")
        u_facade = building['thZones']['livingSpace']['opaquePlanes']['facade']['uValue']
        u_roof = building['thZones']['livingSpace']['opaquePlanes']['roof']['uValue']
        u_floor = building['thZones']['livingSpace']['opaquePlanes']['floor']['uValue']
        #graph = prepare_graph(u_facade, u_roof, u_floor)
        return False, "success", u_facade, u_roof, u_floor
    
    # disable button if one input field is empty
    if u_facade == None or u_roof == None or u_floor == None:
        if u_facade == None: u_facade = 0
        if u_roof == None: u_roof = 0
        if u_floor == None: u_floor = 0
        #graph = prepare_graph(u_facade, u_roof, u_floor)
        if u_facade == 0: u_facade = None
        if u_roof == 0: u_roof = None
        if u_floor == 0: u_floor = None
        return True, "primary", u_facade, u_roof, u_floor

    # save u_values to building on button click
    if button_id == "materials_done_button_id":
        building = read_building_data_yaml(userID='userID')
        building['thZones']['livingSpace']['opaquePlanes']['facade']['uValue'] = u_facade
        building['thZones']['livingSpace']['opaquePlanes']['roof']['uValue'] = u_roof
        building['thZones']['livingSpace']['opaquePlanes']['floor']['uValue'] = u_floor
        save_building_data_yaml(building)
    
        #graph = prepare_graph(u_facade, u_roof, u_floor)
        return False, "success", u_facade, u_roof, u_floor

    # activate button if all inputs are filled
    else:
        return False, "primary", u_facade, u_roof, u_floor

def prepare_graph(u_facade, u_roof, u_floor):

    # read building facade area
    building = read_building_data_yaml(userID='userID')
    facadeArea = building['thZones']['livingSpace']['opaquePlanes']['facade']['area']
    roofArea = building['thZones']['livingSpace']['opaquePlanes']['roof']['area']
    floorArea = building['thZones']['livingSpace']['opaquePlanes']['floor']['area']
    #u_facade = building['thZones']['livingSpace']['opaquePlanes']['facade']['uValue']
    #u_roof = building['thZones']['livingSpace']['opaquePlanes']['roof']['uValue']
    #u_floor = building['thZones']['livingSpace']['opaquePlanes']['floor']['uValue']
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


    graph = create_graph(df)
    return graph