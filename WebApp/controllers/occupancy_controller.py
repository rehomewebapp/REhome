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
    Output("infNumber_id", "value"),
    Output("ventNumber_id", "value"),
    Input("comfortTemp_id", "value"),
    Input("internalGains_id", "value"),
    Input("infNumber_id", "value"),
    Input("ventNumber_id", "value")
    )
def inputDone(comfortTemp, internalGains, infNumber, ventNumber):
    if comfortTemp == None and internalGains == None and infNumber == None and ventNumber == None:
        # ToDo make this more generic! dont use name of thZones, loop through zones instead and calc avg. temp of heatedzones
        building = read_building_data_yaml("userID")
        comfortTemp = building['thZones']['livingSpace']['tempIn']
        internalGains = building['thZones']['livingSpace']['gainsInt']
        infNumber = building['thZones']['livingSpace']['nInf']
        ventNumber = building['thZones']['livingSpace']['nVent']
        return False, "success", comfortTemp, internalGains , infNumber, ventNumber
        #raise PreventUpdate()

    if comfortTemp == None or internalGains == None or infNumber == None or ventNumber == None:
        return True, "primary", comfortTemp, internalGains , infNumber, ventNumber

    # save u_values to building
    building = read_building_data_yaml(userID='userID')
    building['thZones']['livingSpace']['tempIn'] = comfortTemp
    building['thZones']['livingSpace']['gainsInt'] = internalGains
    building['thZones']['livingSpace']['nInf'] = infNumber
    building['thZones']['livingSpace']['nVent'] = ventNumber
    save_building_data_yaml(building)


    return False, "success", comfortTemp, internalGains , infNumber, ventNumber









if __name__ == '__main__':
    app.run_server(debug=True)