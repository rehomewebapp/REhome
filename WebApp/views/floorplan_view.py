import dash_html_components as html
import dash_leaflet as dl

from views.templates.createLayout import create_layout


dummy_pos = [0, 0] # Initial position for marker, polyline and polygon


# Marker icon
icon = {
    "iconUrl": '/assets/bullseye.png',
    "iconSize": [48, 48],  # Size of the icon
    "iconAnchor": [24, 24],  # Anchor of the icon 
}


content = html.Div(children=[
    dl.Map(id = "floorplan_map",
        children=[
                dl.TileLayer(maxZoom = 21, maxNativeZoom = 19),
                dl.GestureHandling(), 
                dl.Marker(id="marker_id", position = dummy_pos, icon=icon, interactive=False), # Start Marker
                dl.Polyline(id="polyline-id", positions=[dummy_pos]),  # Create a polyline
                dl.Polygon(id="polygon-id", positions=[dummy_pos]),  # Create a polygon
            ],
        style={'width': '100%', 'height': '50vh', 'margin': "auto","padding-right":"15px", "display": "block", "position": "relative"}
    ),
    html.Div(id = "area_output", children=""),
    html.Div(id = "hidden_div_id"), # used to trigger "pageload event" see floorplan_controller.py
])


layout = create_layout("floorplan", "/occupancy", "Trace the outline of your building", "/geometry", content)
