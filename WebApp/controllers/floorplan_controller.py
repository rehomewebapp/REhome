from app import app
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from models.building.buildingFactory import read_building_data, save_building_data
from models.building.geometry import floorplane_from_geopolygone, perimeter_from_geopolygone


# callback to center location
@app.callback(
    Output('floorplan_map','center'),
    Output('floorplan_map','zoom'),
    Input('hidden_div_id','children'),
)
def setCenterAndView(hidden_div):
    # onPageLoad-event would be nicer than a hidden div to trigger the callback
    # using this suggested solution for now:
    # https://community.plotly.com/t/trigger-callback-when-a-page-loads-in-order-to-update-all-plots-inputs/10001
    building = read_building_data("userID")
    loc = building["location"]
    center = [float(loc['latitude']),float(loc['longitude'])]
    zoom = 20
    return center, zoom

dummy_pos = [0, 0] # initialize position for marker, polylines and polygone
dlatlon2 = 1e-10  # Controls tolerance of closing click

# callback for drawing the floorplan
@app.callback([Output("polyline-id", "positions"),
               Output("polygon-id", "positions"),
               Output("marker_id","position"),
               Output("area_output","children")],
              [Input("floorplan_map", "click_lat_lng")],
              [State("polyline-id", "positions")])
def update_polyline_and_polygon(click_lat_lng, positions):
    if click_lat_lng is None or positions is None:
        raise PreventUpdate()
    # On first click, reset the polyline and place the start marker
    if len(positions) == 1 and positions[0] == dummy_pos:
        start_marker_position = click_lat_lng
        return [click_lat_lng], [dummy_pos], start_marker_position, ""
    # If the click is close to the first point, close the polygon, 
    # and hide the marker.
    #print(click_lat_lng)
    dist2 = (positions[0][0] - click_lat_lng[0]) ** 2 + (positions[0][1] - click_lat_lng[1]) ** 2
    if dist2 < dlatlon2:
        perimeter = perimeter_from_geopolygone(positions)
        area = floorplane_from_geopolygone(positions)

        building = read_building_data("userID")
        # create a new thermal zone
        building['thZones'] = {'tz0':{'floorArea':area, 'perimeter':perimeter}}
        save_building_data(building)
        return [dummy_pos], positions, [0,0], f"{area=}m^2" # last return sets marker somewhere invisible
    # Otherwise, append the click position.
    positions.append(click_lat_lng)
    return positions, [dummy_pos], positions[0], ""

if __name__ == '__main__':
    app.run_server(debug=True)