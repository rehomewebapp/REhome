
import dash
from dash_bootstrap_components._components.NavItem import NavItem
import dash_html_components as html
import dash_bootstrap_components as dbc


REHOME_LOGO = "/assets/Logo_med_gray.png"
MENU_OPEN = "/assets/menu-open.svg"


def create_navbar(active_page):
    if active_page != "home":
        navbar = dbc.Navbar(
            [
                html.A(
                    dbc.Row(
                        [   
                            dbc.Col(html.Img(src=MENU_OPEN),width = 1),
                            dbc.Col(html.A(
                                html.Img(src=REHOME_LOGO, height="48px"), href="/"),
                            width=3),
                            dbc.Col(html.H2(children=active_page, className="light"), width = 8),
                        ],
                        align="center",
                    ),
                ),
            ],color="primary", #dark=True,
        )
    else:
        navbar = dbc.Navbar(
            [
                html.A(
                    dbc.Row(
                        [   
                            dbc.Col(html.Img(src=REHOME_LOGO, height="48px")),
                        ],
                        align="center",
                    ),
                    href="/",
                ),
            ],color="primary", dark=True,
        )
    
    return navbar