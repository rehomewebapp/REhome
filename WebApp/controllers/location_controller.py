from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash_leaflet as dl


from app import app
from models.building import location

# CONTROLLER

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



@app.callback(
    Output('location_output','children'),

    Input('submit_button','n_clicks'),
    State('input','value')
)
def handle_location(n_clicks, value):
    #print('hello from handle_location')
    if n_clicks == 0:
        return ''
    loc = location.conv_zip_to_location(value)
    if loc == None:
        return f'Sorry we could not find that location.'
    try:
        location.save_location_data(loc)
    except:
        #print("could not save location.")
        pass
    city = loc['city']
    #data = weather.get_weather(loc)
    return ""




if __name__ == '__main__':
    app.run_server(debug=True)