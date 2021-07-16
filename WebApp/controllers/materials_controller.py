from dash.dependencies import Input, Output
from app import app
from models.building import physics, geometry
from dash.exceptions import PreventUpdate
from models.building.buildingFactory import save_building_data, read_building_data
from models.building.utilities import read_tmy_data


@app.callback(
    Output("materials_output_id","children"),
    Input("u_facade_id", "value"),
)
def handle_facade(u_value):
    if u_value == None:
        raise PreventUpdate()

    # save u_value to building
    building = read_building_data(userID='userID')
    building['thZones']['tz0']['opaquePlanes']['facade']['u-value'] = u_value
    save_building_data(building)
    
    # read building facade area
    building = read_building_data(userID='userID')
    facadeArea = building['thZones']['tz0']['opaquePlanes']['facade']['area']
    #load ambient temperature
    tempAmb = read_tmy_data("userID")['T2m']

    #TO DO: load comfort temp (and add to view occupancy)
    temp_comfort=20
    

    heatflow_trans_facade = physics.transmission(u_value, facadeArea, temp_comfort, tempAmb)
    heatflowSum = heatflow_trans_facade.sum()

    physics.heatDemand()
    return f'{heatflowSum = } W'