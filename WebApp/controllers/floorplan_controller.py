from app import app
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from models.building import location

dummy_pos = [0, 0]
dlatlon2 = 1e-11  # Controls tolerance of closing click

# callback to zoom to location
@app.callback(
    Output('floorplan_map','center'),
    Output('floorplan_map','zoom'),
    Input('floorplan_heading','n_clicks'),
)
def set_latlng(n_clicks):
    #print('hello from set_latlng')
    loc = location.read_location_data()
    center = [float(loc['latitude']),float(loc['longitude'])]
    zoom = 13
    return center, zoom

# callback for drawing the floorplan
@app.callback([Output("polyline-id", "positions"),
               Output("polygon-id", "positions"),
               Output("marker_id","position")],
              [Input("floorplan_map", "click_lat_lng")],
              [State("polyline-id", "positions")])
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