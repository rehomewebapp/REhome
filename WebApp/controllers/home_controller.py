from dash.dependencies import Input, Output
from app import app
from dash.exceptions import PreventUpdate
from models.building import buildingFactory, utilities

@app.callback(
    Output("home_output_id","children"),
    Input("start_button_id", "n_clicks")
)
def initBuilding(n_clicks):
    if n_clicks == 0:
        raise PreventUpdate()
    building = buildingFactory.createBuilding()
    utilities.save_building_data(building)
    return ""