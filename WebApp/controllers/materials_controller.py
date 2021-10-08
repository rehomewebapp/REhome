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
    Output("u_window_id", "value"),
    Output("g_window_id", "value"),
    Input("u_facade_id", "value"),
    Input("u_roof_id", "value"),
    Input("u_floor_id", "value"),
    Input("u_window_id", "value"),
    Input("g_window_id", "value"),
    Input("materials_done_button_id", "n_clicks"),
)
def inputDone(u_facade, u_roof, u_floor, u_window, g_window, n_clicks):

    ctx = callback_context
    # check which input has triggered the callback
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    # on pageload: fill input fields with building data
    if not ctx.triggered:
        building = read_building_data_yaml("userID")
        u_facade = building['thZones']['livingSpace']['opaquePlanes']['facade']['uValue']
        u_roof = building['thZones']['livingSpace']['opaquePlanes']['roof']['uValue']
        u_floor = building['thZones']['livingSpace']['opaquePlanes']['floor']['uValue']
        u_window = building['thZones']['livingSpace']['transPlanes']['windowA']['uValue']
        g_window = building['thZones']['livingSpace']['transPlanes']['windowA']['gValue']
        
        return False, "success", u_facade, u_roof, u_floor, u_window, g_window
    
    # disable button if one input field is empty
    if not u_facade or not u_roof or not u_floor or not u_window or not g_window:
        return True, "primary", u_facade, u_roof, u_floor, u_window, g_window

    # save u_values to building on button click
    if button_id == "materials_done_button_id":
        building = read_building_data_yaml(userID='userID')
        building['thZones']['livingSpace']['opaquePlanes']['facade']['uValue'] = u_facade
        building['thZones']['livingSpace']['opaquePlanes']['roof']['uValue'] = u_roof
        building['thZones']['livingSpace']['opaquePlanes']['floor']['uValue'] = u_floor

        for window in building['thZones']['livingSpace']['transPlanes']:
            building['thZones']['livingSpace']['transPlanes'][window]['uValue'] = u_window
            building['thZones']['livingSpace']['transPlanes'][window]['gValue'] = g_window

        save_building_data_yaml(building)
    
        return False, "success", u_facade, u_roof, u_floor, u_window, g_window

    # activate button if all inputs are filled
    else:
        return False, "primary", u_facade, u_roof, u_floor, u_window, g_window

