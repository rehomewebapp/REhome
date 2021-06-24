import dash
import dash_leaflet as dl
import dash_html_components as html

from dash.dependencies import Output, Input, State
from dash.exceptions import PreventUpdate

MAP_ID = "map-id"
MARKER_ID = "marker_id"
POLYLINE_ID = "polyline-id"
POLYGON_ID = "polygon-id"

dummy_pos = [0, 0]
dlatlon2 = 1e-10  # Controls tolerance of closing click

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

icon = {
    "iconUrl": '/assets/bullseye.png',
    "iconSize": [48, 48],  # size of the icon
    "iconAnchor": [24, 24],  # point of the icon which will correspond to marker's location
    "popupAnchor": [-3, -76]  # point from which the popup should open relative to the iconAnchor
}

app = dash.Dash(external_stylesheets=external_stylesheets)
app.layout = html.Div([
    html.H1(children='Locate your home on the map and trace the outline.'),
    dl.Map(id=MAP_ID, center=[48.0062, 8.0378], zoom=10, children=[
        dl.TileLayer(maxZoom = 21, maxNativeZoom = 19), # Map tiles, defaults to OSM
        dl.Marker(id=MARKER_ID,position=dummy_pos, icon=icon, interactive=False),  
        dl.Polyline(id=POLYLINE_ID, positions=[dummy_pos]),  # Create a polyline, cannot be empty at the moment
        dl.Polygon(id=POLYGON_ID, positions=[dummy_pos]),  # Create a polygon, cannot be empty at the moment
    ], style={'width': '1000px', 'height': '500px'}),
])


@app.callback([Output(POLYLINE_ID, "positions"),
               Output(POLYGON_ID, "positions"),
               Output(MARKER_ID,"position")],
              [Input(MAP_ID, "click_lat_lng")],
              [State(POLYLINE_ID, "positions")])
def update_polyline_and_polygon(click_lat_lng, positions):
    if click_lat_lng is None or positions is None:
        raise PreventUpdate()
    # On first click, reset the polyline and place the start marker
    if len(positions) == 1 and positions[0] == dummy_pos:
        start_marker_position = click_lat_lng
        return [click_lat_lng], [dummy_pos], start_marker_position
    # If the click is close to the first point, close the polygon, 
    # and hide the marker.
    print(click_lat_lng)
    dist2 = (positions[0][0] - click_lat_lng[0]) ** 2 + (positions[0][1] - click_lat_lng[1]) ** 2
    if dist2 < dlatlon2:
        print('done')
        return [dummy_pos], positions, [0,0]
    # Otherwise, append the click position.
    positions.append(click_lat_lng)
    return positions, [dummy_pos], positions[0]




if __name__ == '__main__':
    app.run_server(debug=True)