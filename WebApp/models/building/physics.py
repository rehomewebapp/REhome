#constant values
DENSITYAIR = 1.25 # kg/m^3 density of air
HEATCAPAIR = 1100 # J/kgK  specific heat capacity of air


def transmission(uValue, area, tempIn, tempAmb):
    '''Calculate the transmission losses through a construction element.

    .. math::

        \{Q} = U \cdot A \cdot (T_{in} - T_{amb})

    :param uValue: Heat transfer coefficient :math:`U` [W/m^2K]
    :type uValue: float
    :param area: Area of the construction element :math:`A` [m^2]
    :type area: float
    :param tempIn: Temperature inside of the const. element :math: `T_{in}` [°C]
    :type tempIn: float
    :param tempAmb: Temperature outside of the const. element :math: `T_{amb}` [°C]
    :type tempAmb: float
    :return: Heatflow through the construction element :math: `\dot{Q}` [W]
    :rtype: float
    '''

    heatFlow = uValue * area * (tempIn - tempAmb)
    return heatFlow


def solarGains(gValue, area, irrad):
    '''Calculate the solar gains through a transparent construction element.

    .. math::

        \{Q} = g \cdot A \cdot G_{n}

    :param gValue: Solar heat gain coefficient :math:`g` [-]
    :type gValue: float
    :param area: Area of the construction element :math:`A` [m^2]
    :type area: float
    :param irrad: irradiation perpendicular to the construction element :math: `G_{n}` [W/m^2]
    :type irrad: float
    :return: Heatflow through the construction element :math: `\dot{Q}` [W]
    :rtype: float
    '''

    heatFlow = gValue * area * irrad
    return heatFlow

def infAndVent(n, volume, tempIn, tempAmb):
    '''Calculate the infiltration and/or ventilation losses of a volume.

    .. math::

        \dot{Q} = n \cdot V \cdot \rho \cdot c_{P,air} \cdot (T_{in} - T_{amb})

    :param n: Ventilation/Infiltration rate :math:`n` [1/h]
    :type n: float
    :param volume: Volume of the construction element :math:`V` [m^3]
    :type volume: float
    :param tempIn: Temperature inside of the volume :math: `T_{in}` [°C]
    :type tempIn: float
    :param tempAmb: Temperature outside of the volume :math: `T_{amb}` [°C]
    :type tempAmb: float
    :return: Heatflow through the construction element :math: `\dot{Q}` [W]
    :rtype: float
    '''

    heatFlow = n * volume * DENSITYAIR * HEATCAPAIR * (tempIn - tempAmb) / 3600
    return heatFlow

def energyBalance(gains = [], losses = []):
    '''Calculate the energy balance.

    .. math::

        Q = \sum{Q_{loss} - \sum{Q_{gain}}}

    :param gains: All heat gains of the building. [Wh]
    :type gains: list (float)
    :param losses: All heat losses of the building. [Wh]
    :type losses: list (float)
    :return: Heating (+)/Cooling (-) demand. [Wh] 
    :rtype: float
    '''
    sum = 0
    for gain in gains:
        sum -= gain
    for loss in losses:
        sum += loss
    return sum
