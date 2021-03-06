from dash.dependencies import Input, Output
from app import app
from dash.exceptions import PreventUpdate
from models.building.buildingFactory import read_building_data_yaml, save_building_data_yaml
from models.building.utilities import get_tmy_data, save_tmy_data

@app.callback(
    Output("home_output_id","children"),
    Input("start_button_id", "n_clicks")
)
def initBuilding(n_clicks):
    if n_clicks == 0:
        raise PreventUpdate()
    building = read_building_data_yaml('simpleBuilding')
    building['id'] = 'userID'
    save_building_data_yaml(building)
    return ""