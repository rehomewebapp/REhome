import dash
import dash_html_components as html
import dash_bootstrap_components as dbc


# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 52,
    "left": 0,
    "bottom": 0,
    "width": "8rem",
    "height": "100%",
    "z-index": 1,
    "overflow-x": "hidden",
    "transition": "all 0.5s",
    #"padding": "0.5rem 1rem",
    #"color": "secondary",
    "background-color": "#eee",
}

sidebar = html.Div(
    [
        dbc.Nav(
            [
                dbc.NavLink("Building", href="/page-1", id="page-1-link"),
                dbc.NavLink("Renovation", href="/page-2", id="page-2-link"),
                dbc.NavLink("System", href="/page-3", id="page-3-link"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    id="sidebar",
    style=SIDEBAR_STYLE,
)