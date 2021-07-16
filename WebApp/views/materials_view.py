
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from views.templates.footer import footer
from views.templates.header import create_navbar
from views.templates.sidebar import create_sidebar
from views.templates.content_navigation import create_content_nav

content_nav = create_content_nav("materials","/geometry", "Enter the material properties of your building", "/404")
navbar = create_navbar("Materials")
sidebar = create_sidebar("materials")

input = dbc.Row(
    [
        dbc.Col(
            dbc.FormGroup(
                [
                    dbc.Label("Heat transfer coefficient of the facade (U-value)", html_for="u_facade_id"),
                    dbc.Input(
                        type="number",
                        id="u_facade_id",
                        placeholder="U-value [W/m^2K]",
                    ),
                ]
            ),
            width=6,
        ),
    ],
    form=True,
)

output = html.Div("", id = "materials_output_id")

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