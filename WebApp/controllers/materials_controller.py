from dash.dependencies import Input, Output
import pandas as pd
import datetime
from app import app
from models.building import physics, geometry
from dash.exceptions import PreventUpdate
from models.building.buildingFactory import save_building_data, read_building_data
from models.building.utilities import read_tmy_data
from views.templates.graphs import create_graph


@app.callback(
    Output("materials_output_id","children"),
    Output('materials_done_button_id', 'disabled'), 
    Output('materials_done_button_id', 'color'),
    Input("u_facade_id", "value"),
    Input("u_roof_id", "value"),
    Input("u_floor_id", "value"),
)
def handle_facade(u_facade, u_roof, u_floor):
    if u_facade == None or u_roof == None or u_floor == None:
        raise PreventUpdate()

    # save u_values to building
    building = read_building_data(userID='userID')
    building['thZones']['tz0']['opaquePlanes']['facade']['u-value'] = u_facade
    building['thZones']['tz0']['opaquePlanes']['roof']['u-value'] = u_roof
    building['thZones']['tz0']['opaquePlanes']['floor']['u-value'] = u_floor
    save_building_data(building)
    
    # read building facade area
    building = read_building_data(userID='userID')
    facadeArea = building['thZones']['tz0']['opaquePlanes']['facade']['area']
    #load weather data
    index = pd.date_range(datetime.datetime(2021,1,1), periods=8760, freq="h")
    #data = read_tmy_data("userID")
    tempAmb = read_tmy_data("userID")['T2m']
    tempAmb.index = index
    
    #TO DO: load comfort temp (and add to view occupancy)
    temp_comfort=20
    #temperature = data['T2m']
    df = pd.DataFrame(index = index)
    df['Qflow_trans'] = physics.transmission(u_facade, facadeArea, temp_comfort, tempAmb)
    
    graph = create_graph(df)


    heatflowSum = df['Qflow_trans'].sum()/1000 
    #physics.heatDemand()
    return [f'Transmission losses: {heatflowSum:.2f} kWh/a', u_facade, u_roof, u_floor , graph], False, "success"