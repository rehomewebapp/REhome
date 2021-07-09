
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from views.templates.footer import footer
from views.templates.header import create_navbar
from views.templates.sidebar import sidebar

navbar = create_navbar("Materials")

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
            ],width=10,style={"padding-left":"0px"})
        ],style={"margin-right":"0px"}),
    ]),
    footer,
])