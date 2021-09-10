from dash.dependencies import Input, Output
from dash import callback_context

from app import app
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
    Input("ventNumber_id", "value"),
    Input("occupancy_done_button_id", "n_clicks"),
    )
def inputDone(comfortTemp,internalGains,infNumber,ventNumber,clicks):
    ctx = callback_context
    # check which input has triggered the callback
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    # on pageload: fill input fields with building data
    if not ctx.triggered:
        # ToDo make this more generic! dont use name of thZones, loop through zones instead and calc avg. temp of heatedzones
        building = read_building_data_yaml("userID")
        comfortTemp = building['thZones']['livingSpace']['tempIn']
        internalGains = building['thZones']['livingSpace']['gainsInt']
        infNumber = building['thZones']['livingSpace']['nInf']
        ventNumber = building['thZones']['livingSpace']['nVent']
        return False, "success", comfortTemp, internalGains , infNumber, ventNumber
    
    # disable button if one input field is empty
    if comfortTemp == None or internalGains == None or infNumber == None or ventNumber == None:
        return True, "primary", comfortTemp, internalGains , infNumber, ventNumber
   
    # save building data on button click
    if button_id == "occupancy_done_button_id":
        building = read_building_data_yaml(userID='userID')
        building['thZones']['livingSpace']['tempIn'] = comfortTemp
        building['thZones']['livingSpace']['gainsInt'] = internalGains
        building['thZones']['livingSpace']['nInf'] = infNumber
        building['thZones']['livingSpace']['nVent'] = ventNumber
        save_building_data_yaml(building)
        return False, "success", comfortTemp, internalGains , infNumber, ventNumber

    # activate button if all inputs are filled
    else: 
        return False, "primary", comfortTemp, internalGains , infNumber, ventNumber 