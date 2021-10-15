SPEC_CO2_EMISSIONS_GAS_2020 = 200.8 # [g/kWh]
SPEC_CO2_EMISSIONS_EL_2020 = 402.9 # [g/kWh]

def calc_co2_emissions(demand_gas, demand_el):
    ''' This function calculates the CO2 emissions associated with the consumption of gas and electricity.
    
    Parameters
    ---------
    demand_gas: dict
        dictionary containing gas consumptions :math:`E_{gas}~[Wh]
    
    demand_el: dict
        dictionary containing electricity consumptions :math:`E_{el}~[Wh]

    Returns
    -------
    dict of floats
        dictionary containing CO2 emissions for gas consumptions :math:`M_{CO2,gas}~[kg]

    dict of floats
        dictionary containing CO2 emissions for electricity consumptions :math:`M_{CO2,el}~[kg]

    Notes
    -----
    .. math::
        M_{CO2} = m_{spec,CO2} \cdot E

    '''

    co2_gas = {}
    for demand in demand_gas:
        co2_gas[demand] = SPEC_CO2_EMISSIONS_GAS_2020 * demand_gas[demand] / 1000000

    co2_el = {}
    for demand in demand_el:
        co2_el[demand] = SPEC_CO2_EMISSIONS_EL_2020 * demand_el[demand] / 1000000

    return co2_gas, co2_el