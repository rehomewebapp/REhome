import dash_html_components as html
import dash_bootstrap_components as dbc

from views.templates.createLayout import create_layout


uFacadeInput = dbc.Col(
                dbc.FormGroup([
                    dbc.Label("Heat transfer coefficient of the facade (U-value) [W/m^2K]", html_for="u_facade_id"),
                    dbc.Input(type="number", id="u_facade_id", placeholder="U-value facade ")
                ]),
        )

uRoofInput = dbc.Col(
                dbc.FormGroup([
                    dbc.Label("Heat transfer coefficient of the roof (U-value) [W/m^2K]", html_for="u_roof_id"),
                    dbc.Input(type="number", id="u_roof_id", placeholder="U-value roof ")
                ]),
        )

uFloorInput = dbc.Col(
                dbc.FormGroup([
                    dbc.Label("Heat transfer coefficient of the floor (U-value) [W/m^2K]", html_for="u_floor_id"),
                    dbc.Input(type="number", id="u_floor_id", placeholder="U-value floor ")
                ]),
        )


input = html.Div([
            uFacadeInput,
            uRoofInput,
            uFloorInput,
            ]
)


output = html.Div("", id = "materials_output_id")

content= html.Div([input, output])

layout = create_layout("materials","/geometry", "Enter the material properties of your building", "/about_us", content)