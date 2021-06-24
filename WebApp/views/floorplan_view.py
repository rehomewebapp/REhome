import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_leaflet as dl

from app import app

dummy_pos = [0, 0] # Initial position for marker, polyline and polygon

# Marker icon
icon = {
    "iconUrl": '/assets/bullseye.png',
    "iconSize": [48, 48],  # Size of the icon
    "iconAnchor": [24, 24],  # Anchor of the icon 
}


# VIEW

layout = html.Div(children=[
    html.H1(children='Floorplan', id = 'floorplan_heading'),
    html.H2(children='Locate your home on the map and trace the outline.'),
    dl.Map(id = "floorplan_map",
        children=[
                dl.TileLayer(maxZoom = 21, maxNativeZoom = 19), # 
                dl.Marker(id="marker_id", position = dummy_pos, icon=icon, interactive=False), # Start Marker
                dl.Polyline(id="polyline-id", positions=[dummy_pos]),  # Create a polyline
                dl.Polygon(id="polygon-id", positions=[dummy_pos]),  # Create a polygon
            ],
        style={'width': '1000px', 'height': '500px'}
    ),
    dcc.Link('Home', href="/"), # link to landing page
])

if __name__ == '__main__':
    app.run_server(debug=True)