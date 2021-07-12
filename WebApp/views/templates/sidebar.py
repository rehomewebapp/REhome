import dash
from dash_bootstrap_components._components.NavItem import NavItem
import dash_html_components as html
import dash_bootstrap_components as dbc


CHEVRON_UP = "/assets/chevron-up.svg"
CHEVRON_DOWN = "/assets/chevron-down.svg"

def create_sidebar(active_view):
    """Generate a sidebar with the given string as active page"""
    # create dictionary to set active view
    view_states = {
        "location" : False,
        "floorplan":False,
        "geometry" : False,
        "materials" : False,
    }
    # set active page 
    view_states[active_view] = True

    sidebar = html.Div(
        [
            dbc.Nav(
                [   
                    dbc.NavItem(
                        dbc.Row([   
                            dbc.Col(dbc.NavLink("Building", href="/location"),width=8),
                            dbc.Col(html.Img(src=CHEVRON_UP)),
                        ],align="center"), active=True,
                    ),
                    dbc.NavItem(dbc.NavLink("  Location", href="/location",active=view_states["location"])),
                    dbc.NavItem(dbc.NavLink("  Floorplan", href="/floorplan",active=view_states["floorplan"])),
                    dbc.NavItem(dbc.NavLink("  Geometry",href="/geometry",active=view_states["geometry"]),),
                    dbc.NavItem(dbc.NavLink("  Materials",href="/materials",active=view_states["materials"]),),
                    dbc.NavItem(dbc.NavLink("  Occupancy",href="/?", disabled=True),),
                    dbc.NavItem(
                        dbc.Row([   
                            dbc.Col(dbc.NavLink("Renovation", href="/page-2", id="page-2-link"),width=8),
                            dbc.Col(html.Img(src=CHEVRON_DOWN)),
                        ],align="center"), active=False,
                    ),
                    dbc.NavItem(
                        dbc.Row([   
                            dbc.Col(dbc.NavLink("System", href="/page-3", id="page-3-link"),width=8),
                            dbc.Col(html.Img(src=CHEVRON_DOWN)),
                        ],align="center"), active=False,
                    ),
                ],
                vertical=True,
                pills=True,
            ),
        ],style={"background-color":"#eee"},
        id="sidebar",
    )
    return sidebar