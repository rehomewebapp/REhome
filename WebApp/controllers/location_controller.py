from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash_leaflet as dl


from app import app
from models.building import utilities

# create marker and change button style
@app.callback(
    Output("layer", "children"),
    Output('location_done_button_id', 'disabled'), 
    Output('location_done_button_id', 'color'), 
    Input("map", "click_lat_lng")
    )
def map_click(click_lat_lng):
    if click_lat_lng == None:
        raise PreventUpdate()
    marker = [dl.Marker(position=click_lat_lng)]
    return marker, False, "success"


# save location data and download weather data
@app.callback(
    Output('location_output','children'),
    Input('location_done_button_id','n_clicks'),
    State("map", "click_lat_lng")
)
def handle_location(n_clicks, loc):
    if n_clicks == 0:
        raise PreventUpdate()
    if n_clicks == 0:
        return ''
    try:
        utilities.save_location_data(loc, "models/building/data/")
    except:
        pass
    #data = utilities.get_tmy_data(loc[0],loc[1])
    #utilities.save_tmy_data(data)
    return ""




if __name__ == '__main__':
    app.run_server(debug=True)