import dash
from dash_bootstrap_components._components.Row import Row
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_leaflet as dl

from views.templates.header import create_navbar
from views.templates.sidebar import create_sidebar
from views.templates.content_navigation import create_content_nav
from views.templates.footer import footer

from app import app


navbar = create_navbar("Location")
sidebar = create_sidebar("location")
content_nav = create_content_nav("location","", "Click to place a marker on your home", "/occupancy")

# CREATE THE MAP
content = html.Div(children=[
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

layout = html.Div(children=[
    navbar,
    html.Div([
        dbc.Row([
            dbc.Col(sidebar,width = 2),
            dbc.Col([
                content,
                content_nav,
            ],width=10,style={"padding-left":"0px", "text-align" : "center"})
        ],style={"margin-right":"0px"}),
    ]),
    html.Hr(),
    footer,
])

if __name__ == '__main__':
    app.run_server(debug=True)