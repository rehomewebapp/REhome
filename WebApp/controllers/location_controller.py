from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from dash import callback_context
import dash_leaflet as dl


from app import app
from models.building import utilities
from models.building.buildingFactory import read_building_data_yaml, save_building_data_yaml

# create marker and change button style
# save location data and download weather data
@app.callback(
    Output("layer", "children"),
    Output('location_done_button_id', 'disabled'), 
    Output('location_done_button_id', 'color'), 
    Input("map", "click_lat_lng"),
    Input('location_done_button_id','n_clicks'),
    State("map", "click_lat_lng"),
    )
def map_click(click_lat_lng, n_clicks, click_lat_lng_state):
    ctx = callback_context
    # on page load read default loc data and set marker
    if not ctx.triggered:
        button_id = 'No clicks yet'
        location = list(read_building_data_yaml('userID')['location'].values())
        marker = dl.Marker(position=location)
        return marker, False, "success"
    # check which input has triggered the callback
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    # handle click on map -> set marker position
    if button_id == "map":
        marker = [dl.Marker(position=click_lat_lng)]
        return marker, False, "primary"
    # handle save button
    elif button_id == "location_done_button_id":
        print("save button pressed")
        building = read_building_data_yaml('userID')
        building["location"] = {
            "latitude": click_lat_lng_state[0],
            "longitude": click_lat_lng_state[1],
        }
        save_building_data_yaml(building)
        marker = [dl.Marker(position=click_lat_lng)]

        # download weather data and save
        data = utilities.get_tmy_data(loc[0],loc[1])
        utilities.save_tmy_data(data)
        return marker, False, "success"
    else: 
        print("This shoud never happen...")
