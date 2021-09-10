from app import app
from dash.dependencies import Input, Output
from dash import callback_context

from models.building.buildingFactory import save_building_data_yaml, read_building_data_yaml



@app.callback(
    Output('materials_done_button_id', 'disabled'), 
    Output('materials_done_button_id', 'color'),
    Output("u_facade_id", "value"),
    Output("u_roof_id", "value"),
    Output("u_floor_id", "value"),
    Input("u_facade_id", "value"),
    Input("u_roof_id", "value"),
    Input("u_floor_id", "value"),
    Input("materials_done_button_id", "n_clicks"),
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
    
        return False, "success", u_facade, u_roof, u_floor

    # activate button if all inputs are filled
    else:
        return False, "primary", u_facade, u_roof, u_floor

