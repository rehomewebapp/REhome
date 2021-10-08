import dash_html_components as html
import dash_bootstrap_components as dbc

from views.templates.createLayout import create_layout


uFacadeInput = dbc.Col(
                dbc.FormGroup([
                    dbc.Label("Facade", html_for="u_facade_id"),
                    dbc.Input(type="number", id="u_facade_id", placeholder="U-value facade ")
                ]), width = 4
        )

uRoofInput = dbc.Col(
                dbc.FormGroup([
                    dbc.Label("Roof", html_for="u_roof_id"),
                    dbc.Input(type="number", id="u_roof_id", placeholder="U-value roof ")
                ]), width = 4
        )

uFloorInput = dbc.Col(
                dbc.FormGroup([
                    dbc.Label("Floor", html_for="u_floor_id"),
                    dbc.Input(type="number", id="u_floor_id", placeholder="U-value floor ")
                ]), width = 4
        )

uWindowInput = dbc.Col(
                dbc.FormGroup([
                    dbc.Label("U-value [W/(m²K)]", html_for="u_window_id"),
                    dbc.Input(type="number", id="u_window_id", placeholder="U-value window ")
                ]), width = 6
        )

gWindowInput = dbc.Col(
                dbc.FormGroup([
                    dbc.Label("g-value [-]", html_for="g_window_id"),
                    dbc.Input(type="number", id="g_window_id", placeholder="g-value window ")
                ]), width = 6
        )


input = html.Div([
            html.H4("Heat transfer coefficient (U-value) of opaque planes [W/(m²K)]"),
            dbc.Row([
                uFacadeInput,
                uRoofInput,
                uFloorInput
            ]),
            html.H4("Windows"),
            dbc.Row([
                uWindowInput,
                gWindowInput,
            ]),
            ]
)



output = html.Div("", id = "materials_output_id")

content= html.Div([input, output])

layout = create_layout("materials","/geometry", "Enter the material properties of your building", "/about_us", content)