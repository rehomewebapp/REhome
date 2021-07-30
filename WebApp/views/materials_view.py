import dash_html_components as html
import dash_bootstrap_components as dbc

from views.templates.createLayout import create_layout


uFacadeInput = dbc.Col(
                dbc.FormGroup([
                    dbc.Label("Heat transfer coefficient of the facade (U-value)", html_for="u_facade_id"),
                    dbc.Input(type="number", id="u_facade_id", placeholder="U-value facade [W/m^2K]")
                ]),
        width=6)

uRoofInput = dbc.Col(
                dbc.FormGroup([
                    dbc.Label("Heat transfer coefficient of the roof (U-value)", html_for="u_roof_id"),
                    dbc.Input(type="number", id="u_roof_id", placeholder="U-value roof [W/m^2K]")
                ]),
        width=6)

uFloorInput = dbc.Col(
                dbc.FormGroup([
                    dbc.Label("Heat transfer coefficient of the floor (U-value)", html_for="u_floor_id"),
                    dbc.Input(type="number", id="u_floor_id", placeholder="U-value floor [W/m^2K]")
                ]),
        width=6)


input = dbc.Row([
            uFacadeInput,
            uRoofInput,
            uFloorInput,
            ],form=True
)


output = html.Div("", id = "materials_output_id")

content= html.Div([input, output])

layout = create_layout("materials","/geometry", "Enter the material properties of your building", "/about_us", content)