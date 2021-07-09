import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_leaflet as dl

from app import app
from views.templates.header import create_navbar
from views.templates.sidebar import create_sidebar
from views.templates.footer import footer

dummy_pos = [0, 0] # Initial position for marker, polyline and polygon

# Marker icon
icon = {
    "iconUrl": '/assets/bullseye.png',
    "iconSize": [48, 48],  # Size of the icon
    "iconAnchor": [24, 24],  # Anchor of the icon 
}


# VIEW
navbar = create_navbar("Floorplan")
sidebar = create_sidebar("floorplan")

content = html.Div(children=[
    html.H1(children='Floorplan', id = 'floorplan_heading'),
    html.H2(children='Trace the outline of your building'),
    dl.Map(id = "floorplan_map",
        children=[
                dl.TileLayer(maxZoom = 21, maxNativeZoom = 19), # 
                dl.Marker(id="marker_id", position = dummy_pos, icon=icon, interactive=False), # Start Marker
                dl.Polyline(id="polyline-id", positions=[dummy_pos]),  # Create a polyline
                dl.Polygon(id="polygon-id", positions=[dummy_pos]),  # Create a polygon
            ],
        style={'width': '100%', 'height': '50vh', 'margin': "auto","padding-right":"15px", "display": "block", "position": "relative"}
    ),
    html.Div(id = "area_output", children=""),

])


layout = html.Div(children=[
    navbar,
    html.Div([
        dbc.Row([
            dbc.Col(sidebar,width = 2),
            dbc.Col([
                content,
            ],width=10,style={"padding-left":"0px", "text-align" : "center"})
        ],style={"margin-right":"0px"}),
    ]),
    html.Hr(),
    footer,
])


if __name__ == '__main__':
    app.run_server(debug=True)