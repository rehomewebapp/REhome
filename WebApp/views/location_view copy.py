import dash
from dash_bootstrap_components._components.Row import Row
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_leaflet as dl

from views.templates.header import create_navbar
from views.templates.sidebar import create_sidebar
from views.templates.footer import footer

from app import app


# CREATE THE MAP

dummy_pos = [0, 0] # Initial position for marker, polyline and polygon

# Marker icon
icon = {
    "iconUrl": '/assets/bullseye.png',
    "iconSize": [48, 48],  # Size of the icon
    "iconAnchor": [24, 24],  # Anchor of the icon 
}


content = html.Div(children=[
    html.H2(children='Find your home on a map and click to place a marker'),
    dl.Map(id = "floorplan_map",  zoom = 2,
        children=[
                dl.TileLayer(maxZoom = 21, maxNativeZoom = 19), # 
                dl.Marker(id="marker_id", position = dummy_pos, icon=icon, interactive=False), # Start Marker
                dl.Polyline(id="polyline-id", positions=[dummy_pos]),  # Create a polyline
                dl.Polygon(id="polygon-id", positions=[dummy_pos]),  # Create a polygon
            ],
        #style={'width': '1000px', 'height': '500px'}
        style={'width': '100%', 'height': '50vh', 'margin': "auto","padding-right":"15px", "display": "block", "position": "relative"}
    ),
    html.Div(id = "area_output", children=""),
])

navbar = create_navbar("Building / Location")
sidebar = create_sidebar("location")

layout = html.Div(children=[
    navbar,
    html.Div([
        dbc.Row([
            dbc.Col(sidebar,width = 2),
            dbc.Col([
                content,
            ],width=10,style={"padding-left":"0px"})
        ],style={"margin-right":"0px"}),
    ]),
    html.Hr(),
    footer,
])

if __name__ == '__main__':
    app.run_server(debug=True)