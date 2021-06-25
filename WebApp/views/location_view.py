import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_leaflet as dl

from views.templates.header import navbar
from views.templates.sidebar import sidebar
from views.templates.footer import footer

#from dash_html_components.Button import Button

from app import app

# CREATE THE USER INPUT 

CONTENT_STYLE = {"margin-left": "9rem"}

content_1 = html.Div(children=[
    html.Div(children='''
        Where is your building located?
    '''),
    dcc.Input(id="input", type="text", placeholder="Enter post code", value = ''),
    dbc.Button("Search", id="submit_button", className='',  n_clicks=0),
    html.Div(id='location_output',children=''),
], style=CONTENT_STYLE)



# CREATE THE MAP

dummy_pos = [0, 0] # Initial position for marker, polyline and polygon

# Marker icon
icon = {
    "iconUrl": '/assets/bullseye.png',
    "iconSize": [48, 48],  # Size of the icon
    "iconAnchor": [24, 24],  # Anchor of the icon 
}


content_2 = html.Div(children=[
    html.H2(children='Locate your home on the map and trace the outline.'),
    dl.Map(id = "floorplan_map",  zoom = 2,
        children=[
                dl.TileLayer(maxZoom = 21, maxNativeZoom = 19), # 
                dl.Marker(id="marker_id", position = dummy_pos, icon=icon, interactive=False), # Start Marker
                dl.Polyline(id="polyline-id", positions=[dummy_pos]),  # Create a polyline
                dl.Polygon(id="polygon-id", positions=[dummy_pos]),  # Create a polygon
            ],
        style={'width': '1000px', 'height': '500px'}
    ),
    html.Div(id = "area_output", children=""),
], style=CONTENT_STYLE)



layout = html.Div(children=[
    navbar,
    sidebar,
    content_1,
    content_2,
    footer,
])

if __name__ == '__main__':
    app.run_server(debug=True)