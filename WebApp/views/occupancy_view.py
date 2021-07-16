
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from views.templates.footer import footer
from views.templates.header import create_navbar
from views.templates.sidebar import create_sidebar
from views.templates.content_navigation import create_content_nav

navbar = create_navbar("Occupancy")
sidebar = create_sidebar("occupancy")
content_nav = create_content_nav("occupancy","/location", "Specify how you use your building", "/floorplan")

input = dbc.Row(
    [
        dbc.Col(
            dbc.FormGroup(
                [
                    dbc.Label("Comfort temperature", html_for="comfortTemp_id"),
                    dbc.Input(
                        type="number",
                        id="comfortTemp_id",
                        placeholder="Comfort temperature [°C]",
                    ),
                ]
            ),
            width=6,
        ),
    ],
    form=True,
)

output = html.Div("", id = "occupancy_output_id")

content= html.Div([input, output])

layout = html.Div(children=[
    navbar,
    html.Div([
        dbc.Row([
            dbc.Col(sidebar,width = 2),
            dbc.Col([
                content,
                content_nav,
            ],width=10,style={"padding-left":"0px"})
        ],style={"margin-right":"0px"}),
    ]),
    footer,
])