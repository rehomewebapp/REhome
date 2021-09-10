import dash_html_components as html
import dash_leaflet as dl

from views.templates.createLayout import create_layout

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
            'height': '50vh', 
            'margin': "auto", 
            "display": "block",
             "position": "relative"
             }

    ),
    html.Div(id = "location_output", children=""),
])


layout = create_layout("location", "", "Click to place a marker on your home", "/occupancy", content)
