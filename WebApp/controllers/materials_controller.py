from dash.dependencies import Input, Output
from app import app
from models.building import physics, geometry
from dash.exceptions import PreventUpdate
from models.building.buildingFactory import save_building_data, read_building_data


@app.callback(
    Output("materials_output_id","children"),
    Input("u_facade_id", "value"),
)
def handle_facade(u_value):
    if u_value == None:
        raise PreventUpdate()

    building = read_building_data(userID='userID')
    building['thZones']['tz0']['opaquePlanes']['facadeArea']['u-value'] = u_value
    save_building_data(building)
    
    # TO DO: load building facade area
    #facadeArea = geometry.read_geometry_data()
    facadeArea = 100
    #TO DO: load comfort temp (and add to view occupancy)
    temp_comfort=20
    # TO DO: load ambient temperature
    temp_amb = 15

    heatflow_trans_facade = physics.transmission(u_value, facadeArea, temp_comfort, temp_amb)

    physics.heatDemand()
    return f'{heatflow_trans_facade = } W'