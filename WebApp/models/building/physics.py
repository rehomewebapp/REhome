#constant values
DENSITYAIR = 1.25 # kg/m^3 density of air
HEATCAPAIR = 1100 # J/kgK  specific heat capacity of air


def transmission(uValue, area, tempIn, tempAmb):
    """Calculate transmission losses through a plane.

    Parameters
    ----------
    uValue : float
        Heat transfer coefficient :math:`U~[W/m^2K]`
    area : float
        Area of the plane :math:`A~[m^2]`
    tempIn : float
        Temperature inside of the plane :math:`T_{in}~[°C]`
    tempAmb : float or series
        Temperature outside of the plane :math:`T_{amb}~[°C]`

    Returns
    -------
    float
        Heatflow through the plane :math:`\dot{Q}~[W]`

    Notes
    -----
    .. math::
        \dot{Q} = U \cdot A \cdot (T_{in} - T_{amb})
    """

    heatFlow = uValue * area * (tempIn - tempAmb)
    return heatFlow


def solarGains(gValue, area, irrad):
    """Calculate the solar gains through a transparent plane.

    Parameters
    ----------
    gValue : float
        Solar heat gain coefficient :math:`g~[-]`
    area : float
        Area of the plane :math:`A~[m^2]`
    irrad : float
        Global irradiation perpendicular to the plane :math:`G_{n}~[W/m^2]`

    Returns
    -------
    float
        Heatflow through the plane :math:`\dot{Q}~[W]`

    Notes
    -----
    .. math::
        \dot{Q} = g \cdot A \cdot G_{n}
    """


    heatFlow = gValue * area * irrad
    return heatFlow

def internalGains(area, specInternalGains):
    """Calculate the internal gains for the heated area.

    Parameters
    ----------
    area : float
        Heated living area :math:`A~[m^2]`
    specInternalGains : float
        Specific internal gains :math:`q_{int}~[W/m^2]`
    
    Returns
    -------
    float
        Heatflow of internal gains :math:`\dot{Q}_{int}~[W]`

    Notes
    -----
    .. math::
        \dot{Q}_{int} = q_{int} \cdot A
    """
    heatFlow = specInternalGains * area
    return heatFlow


def infAndVent(n, volume, tempIn, tempAmb):
    r"""Calculate the infiltration and/or ventilation losses of a volume.

    Parameters
    ----------
    n : float
        Ventilation/Infiltration rate :math:`n~[1/h]`
    volume : float
        Volume of the construction element :math:`V~[m^3]`
    tempIn : float
        Temperature inside of the volume :math:`T_{in}~[°C]`
    tempAmb : float
        Temperature outside of the volume :math:`T_{amb}~[°C]`

    Returns
    -------
    float
        Heatflow through the construction element :math:`\dot{Q}~[W]`

    Notes
    -----
    .. math::
        \dot{Q} = n \cdot V \cdot \rho \cdot c_{P,air} \cdot (T_{in} - T_{amb})
    """


    heatFlow = n * volume * DENSITYAIR * HEATCAPAIR * (tempIn - tempAmb) / 3600
    return heatFlow

def heatDemand(gains = [], losses = []):
    """Calculate the heating or cooling demand using an energy balance.

    Parameters
    ----------
    gains : list of float
        All heat gains of the building.  :math:`Q_{gain}~[Wh]`
    losses : list of float
        All heat losses of the building.  :math:`Q_{loss}~[Wh]`

    Returns
    -------
    float
        Heating (+) or cooling (-) demand. :math:`{Q}~[Wh]`

    Notes
    -----
    .. math::
        Q = \sum{Q_{loss} - \sum{Q_{gain}}}
    """


    sum = 0
    for gain in gains:
        sum -= gain
    for loss in losses:
        sum += loss
    return sum


def heatflow2Energy(heatflow, timestep):
    """Calculate the resulting energy of a heatflow in a certain timestep.

    Parameters
    ----------
    heatflow : float
        Heatflow.  :math:`\dot{Q}~[W]`
    timestep : float
        Timestep.  :math:`\Delta t~[h]`

    Returns
    -------
    float
        Energy. :math:`Q~[Wh]`

    Notes
    -----
    .. math::
        Q = \dot{Q} \cdot \Delta t
    """

    energy = heatflow * timestep
    return energy