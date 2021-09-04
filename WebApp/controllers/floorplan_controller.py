from app import app
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash_leaflet as dl

from models.building.buildingFactory import read_building_data_yaml, save_building_data_yaml
from models.building.geometry import area_from_geopolygone, perimeter_from_geopolygone

from views.floorplan_view import icon

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
    building = read_building_data_yaml("userID")
    loc = building["location"]
    center = [float(loc['latitude']),float(loc['longitude'])]
    zoom = 19
    return center, zoom

dlatlon2 = 1e-10  # Controls tolerance of closing click
floorplanClosed = True

# callback for drawing the floorplan
@app.callback([Output("layer_floorplan_map","children"),
               Output('floorplan_done_button_id', 'disabled'), 
               Output('floorplan_done_button_id', 'color')],
              [Input("floorplan_map", "click_lat_lng")])
def update_polyline_and_polygon(click_lat_lng):
    global floorplanClosed
    # load initial floorplan from file
    building = read_building_data_yaml('userID')
    first_position = building['floorPlan'][0]
    positions = building['floorPlan']
    # on page load
    if click_lat_lng is None:
        polygon = dl.Polygon(id="polygon-id", positions=positions),  
        floorplanClosed = True
        return polygon, False, "success" 

    # On first click, reset the polyline and place the start marker
    if click_lat_lng:
        if floorplanClosed == True:
            start_marker = dl.Marker(id="marker_id", position = click_lat_lng, icon=icon, interactive=False), # Start Marker
            positions = [click_lat_lng]
            building['floorPlan'] = positions
            save_building_data_yaml(building)
            floorplanClosed = False
            return start_marker, True, "primary"

    # If the click is close to the first point, close the polygon and save floorplan information 
    dist2 = (positions[0][0] - click_lat_lng[0]) ** 2 + (positions[0][1] - click_lat_lng[1]) ** 2
    if dist2 < dlatlon2:
        polygone = dl.Polygon(id="polygon-id", positions=positions)
        perimeter = perimeter_from_geopolygone(positions)#
        building['perimeter'] = perimeter
        groundArea = area_from_geopolygone(positions)
        building['groundArea'] = groundArea
        save_building_data_yaml(building)
        floorplanClosed = True
        return polygone, False, "success"

    # Otherwise, append the click position and draw line
    if len(positions) >= 1: 
        polyline = dl.Polyline(id="polyline-id", positions=positions)  # Create a polyline
        positions.append(click_lat_lng)
        building['floorPlan'] = positions
        save_building_data_yaml(building)
        floorplanClosed = False
        return polyline, True, "primary"

if __name__ == '__main__':
    app.run_server(debug=True)