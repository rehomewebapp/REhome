from app import app
from dash.dependencies import Input, Output


from models.building import physics
from models.building.buildingFactory import read_building_data_yaml
from models.building.utilities import read_tmy_data
from views.templates.graphs import create_bar_graph


@app.callback(
    Output('heatDemand_content_id', 'children'),
    Input("update_graphs_button_id", "n_clicks"),
)
#def inputDone(location_clicks, occupancy_clicks, floorplan_clicks, geometry_clicks, materials_clicks):
def inputDone(n_clicks):
    building = read_building_data_yaml(userID='userID')
    weatherdata = read_tmy_data("userID")
    heatflows = physics.heatFlows(building, weatherdata)
    graph = create_bar_graph(heatflows)
    return graph