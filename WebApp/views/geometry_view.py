
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from views.templates.footer import footer
from views.templates.header import create_navbar
from views.templates.sidebar import sidebar

navbar = create_navbar("Geometry")

input = dbc.Row(
    [
        dbc.Col(
            dbc.FormGroup(
                [
                    dbc.Label("Number of storys", html_for="n_storys_id"),
                    dbc.Input(
                        type="number",
                        id="n_storys_id",
                        placeholder="Enter number of storys",
                    ),
                ]
            ),
            width=6,
        ),
        dbc.Col(
            dbc.FormGroup(
                [
                    dbc.Label("Height of the storys in meter", html_for="story_height_id"),
                    dbc.Input(
                        type="number",
                        step=0.01,
                        id="story_height_id",
                        placeholder="Enter height of the storys in meter",
                    ),
                ]
            ),
            width=6,
        ),
    ],
    form=True,
)

output = html.Div("", id = "geometry_output_id")

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