from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash_leaflet as dl


from app import app
from models.building import utilities
from models.building.buildingFactory import read_building_data_yaml, save_building_data_yaml

# create marker and change button style
@app.callback(
    Output('occupancy_done_button_id', 'disabled'), 
    Output('occupancy_done_button_id', 'color'), 
    Output("comfortTemp_id", "value"),
    Output("internalGains_id", "value"),
    Output("infVentNumber_id", "value"),
    Input("comfortTemp_id", "value"),
    Input("internalGains_id", "value"),
    Input("infVentNumber_id", "value")
    )
def inputDone(comfortTemp, internalGains, infVentNumber):
    if comfortTemp == None and internalGains == None and infVentNumber == None:
        # ToDo make this more generic! dont use name of thZones, loop through zones instead and calc avg. temp of heatedzones
        comfortTemp = read_building_data_yaml('userID')['thZones']['livingSpace']['tempIn']
        internalGains = read_building_data_yaml('userID')['thZones']['livingSpace']['gainsInt']
        infVentNumber = read_building_data_yaml('userID')['thZones']['livingSpace']['nVent']
        return False, "success", comfortTemp, internalGains , infVentNumber
        #raise PreventUpdate()

    # save u_values to building
    building = read_building_data_yaml(userID='userID')
    building['thZones']['livingSpace']['tempIn'] = comfortTemp
    building['thZones']['livingSpace']['gainsInt'] = internalGains
    building['thZones']['livingSpace']['nVent'] = infVentNumber
    building['thZones']['livingSpace']['nInf'] = 0
    save_building_data_yaml(building)


    return False, "success", comfortTemp, internalGains , infVentNumber









if __name__ == '__main__':
    app.run_server(debug=True)