import pandas as pd
import datetime
import pvlib

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


def heatFlows(building, weatherdata):
    '''This function calculates the the different heatflows in the building'''

    # Extract relevant building information
    facadeArea = building['thZones']['livingSpace']['opaquePlanes']['facade']['area']
    roofArea = building['thZones']['livingSpace']['opaquePlanes']['roof']['area']
    floorArea = building['thZones']['livingSpace']['opaquePlanes']['floor']['area']
    u_facade = building['thZones']['livingSpace']['opaquePlanes']['facade']['uValue']
    u_roof = building['thZones']['livingSpace']['opaquePlanes']['roof']['uValue']
    u_floor = building['thZones']['livingSpace']['opaquePlanes']['floor']['uValue']
    latitude = building['location']['latitude']
    longitude = building['location']['longitude']
    temp_comfort=building['thZones']['livingSpace']['tempIn']

    # Overwrite index of TMY weatherdata
    index = pd.date_range(datetime.datetime(2021,1,1), periods=8760, freq="h")
    weatherdata.index = index

    #TO DO: find good model for ground temperature
    tempGround = weatherdata['T2m'] * 0.5

    # Calculate solar irradiance on windows
    location = pvlib.location.Location(latitude = latitude,
                                        longitude = longitude,
                                        tz = 'Europe/Berlin', # !TODO get timezone from location
                                        )       

    solarposition = location.get_solarposition(times = index)

    # Calculate window heat flows
    q_flow_trans_window, q_flow_sol_window = 0, 0
    for window in building['thZones']['livingSpace']['transPlanes']:
        area = building['thZones']['livingSpace']['transPlanes'][window]['area']
        u_window = building['thZones']['livingSpace']['transPlanes'][window]['uValue']
        g_window = building['thZones']['livingSpace']['transPlanes'][window]['gValue']
        tilt = building['thZones']['livingSpace']['transPlanes'][window]['tilt']
        azimuth = building['thZones']['livingSpace']['transPlanes'][window]['azimuth']
        #calculate transmission through window
        q_flow_trans_window += transmission(u_window, area, temp_comfort, weatherdata['T2m'])

        poa = pvlib.irradiance.get_total_irradiance(surface_tilt = tilt,
                                                    surface_azimuth = azimuth,
                                                    solar_zenith = solarposition.zenith,
                                                    solar_azimuth = solarposition.azimuth,
                                                    dni = weatherdata['Gb(n)'],
                                                    ghi = weatherdata['G(h)'],
                                                    dhi = weatherdata['Gd(h)'],
                                                    ).poa_global.fillna(0)
        # calculate solar gains through window
        q_flow_sol_window += solarGains(gValue = g_window, area = area, irrad = poa)


    df = pd.DataFrame(index = index)

    df['Qflow_trans_windows'] = q_flow_trans_window
    df['Qflow_sol'] = q_flow_sol_window

    # Caluclate transmission heatflows through opaque elements
    df['Qflow_trans_facade'] = transmission(u_facade, facadeArea, temp_comfort, weatherdata['T2m'])
    df['Qflow_trans_roof'] = transmission(u_roof, roofArea, temp_comfort, weatherdata['T2m'])
    df['Qflow_trans_ground'] = transmission(u_floor, floorArea, temp_comfort, tempGround)


    df['Qflow_int'] = internalGains(area = building['thZones']['livingSpace']['floorArea'], 
                                           specInternalGains= building['thZones']['livingSpace']['gainsInt'])

    df['Qflow_vent'] = infAndVent(n = building['thZones']['livingSpace']['nVent'] + building['thZones']['livingSpace']['nInf'],
                                        volume = building['thZones']['livingSpace']['volume'],
                                        tempIn = temp_comfort,
                                        tempAmb = weatherdata['T2m'])

    gains = [df['Qflow_int'], df['Qflow_sol']]
    losses = [df['Qflow_trans_facade'], df['Qflow_trans_roof'], df['Qflow_trans_ground'], df['Qflow_trans_windows'], df['Qflow_vent']]
    df['heatDemand'] = heatDemand(gains = gains, losses = losses)

    return df