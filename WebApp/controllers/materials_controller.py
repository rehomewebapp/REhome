from dash.dependencies import Input, Output
from app import app
from models.building import physics, geometry
from dash.exceptions import PreventUpdate


@app.callback(
    Output("materials_output_id","children"),
    Input("u_facade_id", "value"),
)
def handle_facade(u_value):
    if u_value == None:
        raise PreventUpdate()

    # TO DO: load ambient temperature
    temp_amb = 15
    # TO DO: load building facade area
    #facadeArea = geometry.read_geometry_data()
    facadeArea = 100
    #TO DO: load comfort temp (and add to view occupancy)
    temp_comfort=20

    heatflow_trans_facade = physics.transmission(u_value, facadeArea, temp_comfort, temp_amb)

    physics.heatDemand()
    return f'{heatflow_trans_facade = } W'