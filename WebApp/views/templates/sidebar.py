import dash
from dash_bootstrap_components._components.NavItem import NavItem
import dash_html_components as html
import dash_bootstrap_components as dbc


CHEVRON_UP = "/assets/chevron-up.svg"
CHEVRON_DOWN = "/assets/chevron-down.svg"

sidebar = html.Div(
    [
        dbc.Nav(
            [   
                dbc.NavItem(
                    dbc.Row([   
                        dbc.Col(dbc.NavLink("Building", href="/views/location_view"),width=8),
                        dbc.Col(html.Img(src=CHEVRON_UP)),
                    ],align="center"), active=True,
                ),
                dbc.NavItem(dbc.NavLink("  Location", href="/views/location_view",active=True)),
                dbc.NavItem(dbc.NavLink("  Geometry",href="/geometry"),),
                dbc.NavItem(dbc.NavLink("  Materials",href="/materials"),),
                dbc.NavItem(dbc.NavLink("  Occupancy",href="/?", disabled=True),),
                #html.Hr(className="my-1"),
                dbc.NavItem(
                    dbc.Row([   
                        dbc.Col(dbc.NavLink("Renovation", href="/page-2", id="page-2-link"),width=8),
                        dbc.Col(html.Img(src=CHEVRON_DOWN)),
                    ],align="center"), active=False,
                ),
                #dbc.NavItem(dbc.NavLink("Renovation", href="/page-2", id="page-2-link")),
                #html.Hr(className="my-1"),
                dbc.NavItem(
                    dbc.Row([   
                        dbc.Col(dbc.NavLink("System", href="/page-3", id="page-3-link"),width=8),
                        dbc.Col(html.Img(src=CHEVRON_DOWN)),
                    ],align="center"), active=False,
                ),
                #dbc.NavItem(dbc.NavLink("System", href="/page-3", id="page-3-link")),
            ],
            #className="secondary",
            vertical=True,
            pills=True,
        ),
    ],style={"background-color":"#eee"},
    id="sidebar",
)