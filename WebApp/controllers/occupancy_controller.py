from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash_leaflet as dl


from app import app
from models.building import utilities
from models.building.buildingFactory import read_building_data, save_building_data

# create marker and change button style
@app.callback(
    Output('occupancy_done_button_id', 'disabled'), 
    Output('occupancy_done_button_id', 'color'), 
    Input("comfortTemp_id", "value"),
    )
def inputDone(comfortTemp):
    if comfortTemp == None:
        raise PreventUpdate()
    return False, "success"







if __name__ == '__main__':
    app.run_server(debug=True)