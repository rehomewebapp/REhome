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

content = html.Div(children=[
    html.H2(children='Click to place a marker on your home'),
    dl.Map(id = "map",  zoom = 2,
        children=[
            # create tile layer, and set high zoom levels
            dl.TileLayer(maxZoom = 21, maxNativeZoom = 19),
            dl.ScaleControl(), # adds scale in bottom left corner
            dl.LayerGroup(id="layer"), # add layer for the marker
        ],
        style={'width': '100%', 'height': '50vh', 'margin': "auto","padding-right":"15px", "display": "block", "position": "relative"}
    ),
    html.Div(id = "location_output", children=""),
])

button = html.P(dbc.Button("Done", color="primary", 
    href="floorplan",
    id="location_done_button_id", n_clicks=0, disabled=True))


navbar = create_navbar("Location")
sidebar = create_sidebar("location")

layout = html.Div(children=[
    navbar,
    html.Div([
        dbc.Row([
            dbc.Col(sidebar,width = 2),
            dbc.Col([
                content,
                button,
            ],width=10,style={"padding-left":"0px", "text-align" : "center"})
        ],style={"margin-right":"0px"}),
    ]),
    html.Hr(),
    footer,
])

if __name__ == '__main__':
    app.run_server(debug=True)