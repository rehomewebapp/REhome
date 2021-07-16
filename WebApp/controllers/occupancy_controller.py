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
    Input("internalGains_id", "value"),
    Input("infVentNumber_id", "value")
    )
def inputDone(comfortTemp, internalGains, infVentNumber):
    if comfortTemp == None or internalGains == None or infVentNumber == None:
        raise PreventUpdate()

    # save u_values to building
    building = read_building_data(userID='userID')
    building['thZones']['tz0']['tempIn'] = comfortTemp
    building['thZones']['tz0']['gainsInt'] = internalGains
    building['thZones']['tz0']['nVent'] = infVentNumber
    building['thZones']['tz0']['nInf'] = 0
    save_building_data(building)


    return False, "success"









if __name__ == '__main__':
    app.run_server(debug=True)