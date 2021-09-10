import dash_html_components as html
import dash_bootstrap_components as dbc

from views.templates.createLayout import create_layout

comfTempInput = dbc.Col(
                dbc.FormGroup([
                    dbc.Label("Comfort temperature [°C]", html_for="comfortTemp_id"),
                    dbc.Input(type="number", id="comfortTemp_id", placeholder="Comfort temperature ")
                ]),
        )

internalGainsInput = dbc.Col(
                dbc.FormGroup([
                    dbc.Label("Internal Gains [W/m^2]", html_for="internalGains_id"),
                    dbc.Input(type="number", id="internalGains_id", placeholder="Internal gains ")
                ]),
        )

infInput = dbc.Col(
                dbc.FormGroup([
                    dbc.Label("Infiltration number [1/h]", html_for="infNumber_id"),
                    dbc.Input(type="number", id="infNumber_id", placeholder="Infiltration number")])
                )
ventInput = dbc.Col(
                dbc.FormGroup([
                    dbc.Label("Ventilation number [1/h]", html_for="ventNumber_id"),
                    dbc.Input(type="number", id="ventNumber_id", placeholder="Ventilation number")])
                )

input = html.Div([
                comfTempInput,
                internalGainsInput,
                infInput,
                ventInput,
            ], 
)

output = html.Div("", id = "occupancy_output_id")

content= html.Div([input, output])


layout = create_layout("occupancy","/location", "Specify how you use your building", "/floorplan", content)