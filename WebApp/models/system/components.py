class Gasboiler():
    '''Simple model of a gasboiler

    Attributes
    ----------
    efficiency: float
        The efficiency of the gas boiler

    Methods
    -------
    calc_used_fuel(power_actual)
        Calculate required fuel consumption to cover the remaining heating demand

    '''
    def __init__(self, efficiency)
        self.efficiency = efficiency

    def calc_used_fuel(self, power_actual): # power_actual [kW]
        '''Calculate required fuel consumption to cover the remaining heating demand [kW]

        Parameters
        ----------
        power_actual: float
            Heating load that has to be covered by the gasboiler :math:`\dot{Q_{th}}~[W]`

        Returns
        -------
        Float
            Required gas to cover the required heating load :math:`E_{gas}~[W]`

        Notes
        -----
        .. math::
            E_{gas} = \frac{\dot{Q_{th}}}{\eta}

        '''
        used_fuel = power_actual / self.efficiency #used_fuel [kW]
        return used_fuel