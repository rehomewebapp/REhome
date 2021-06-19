import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State

from app import app

from models.building import location
#from models.building import weather

# CONTROLLER

@app.callback(
    Output('location_output','children'),
    Input('submit_button','n_clicks'),
    State('input','value')
)
def show_city(n_clicks, value):
    if n_clicks == 0:
        return ''
    loc = location.conv_zip_to_location(value)
    if loc == None:
        return f'Sorry we could not set up a building for that location.'
    city = loc['city']
    #data = weather.get_weather(loc)
    return f'Your building will be placed in {city}.'

if __name__ == '__main__':
    app.run_server(debug=True)