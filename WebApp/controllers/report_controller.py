from dash.dependencies import Input, Output
from dash import callback_context

from app import app

from models.building import physics
from models.building.buildingFactory import read_building_data_yaml
from models.building.utilities import read_tmy_data

from models.system import components

from models.assessment.ecological import calc_co2_emissions

@app.callback(
    Output('emissions_output_id', 'children'),
    Output('shDemand_output_id', 'children'),
    Output('shDemandSpec_output_id', 'children'),
    Input("update_graphs_button_id", "n_clicks"),
)
def update_report(n_clicks):
    building = read_building_data_yaml(userID='userID')
    heatedLivingSpace = building['thZones']['livingSpace']['floorArea']
    weatherdata = read_tmy_data("userID")
    heatdemand_SH = physics.heatFlows(building, weatherdata)['heatDemand'].clip(lower=0).sum()
    gas_boiler = components.Gasboiler(efficiency=0.95)
    gas_SH = gas_boiler.calc_used_fuel(heatdemand_SH)
    demand_gas = {'Gasboiler, SH': gas_SH}
    demand_el = {}
    co2emissionsGas = calc_co2_emissions(demand_gas, demand_el)[0]
    return round(co2emissionsGas['Gasboiler, SH'],0), round(heatdemand_SH/1000,0), round(heatdemand_SH/(1000*heatedLivingSpace),0)
