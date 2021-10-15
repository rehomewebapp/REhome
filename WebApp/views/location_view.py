import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_leaflet as dl

from views.templates.createLayout import create_layout

toast = html.Div(
    [
        dbc.Toast(
            "This toast is placed in the top right",
            id="weather_data_toast_id",
            header="Weather data download",
            is_open=False,
            dismissable=True,
            icon="danger",
            # top: 66 positions the toast below the navbar
            style={"position": "absolute", "top": "30vh", "left": "2rem", "width": 350, "z-index": "500"},
        ),
    ]
)


# CREATE THE MAP
content = html.Div(children=[
    dl.Map(id = "map",  zoom = 2,
        children=[
            # create tile layer, and set high zoom levels
            dl.TileLayer(),
            #dl.TileLayer(maxZoom = 21, maxNativeZoom = 19),
            dl.GestureHandling(),
            dl.LayerGroup(id="layer"), # add layer for the marker
        ],
        style={'width': '100%', 
            'height': 'calc( 48vh - 5.4rem)', 
            'margin': "auto", 
            "display": "flex",
            "position": "relative",
             }

    ),
    html.Div(id = "location_output", children=""),
    toast,
])






layout = create_layout("location", "", "Click to place a marker on your home", "/occupancy", content)
