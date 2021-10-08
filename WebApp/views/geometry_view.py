import dash_html_components as html
import dash_bootstrap_components as dbc

from views.templates.createLayout import create_layout


input = html.Div([   
    html.H4("Stories"),
    dbc.Row([
        dbc.Col(
            dbc.FormGroup(
                [
                    dbc.Label("Number", html_for="n_storys_id"),
                    dbc.Input(
                        type="number",
                        id="n_storys_id",
                        placeholder="Enter number of storys",
                    ),
                ]
            ),
        width=6),
        dbc.Col(
            dbc.FormGroup(
                [
                    dbc.Label("Height [m]", html_for="story_height_id"),
                    dbc.Input(
                        type="number",
                        step=0.01,
                        id="story_height_id",
                        placeholder="Enter height of the storys",
                    ),
                ]
            ),
        width=6),
    ]),
    html.H4("Window area [m²]"),
    dbc.Row([
        dbc.Col(
            dbc.FormGroup(
                [
                    dbc.Label("North", html_for="area_win_a_id"),
                    dbc.Input(
                        type="number",
                        id="area_win_a_id",
                        placeholder="Window area facing north",
                    ),
                ]
            ),
        width=3),
        dbc.Col(
            dbc.FormGroup(
                [
                    dbc.Label("East", html_for="area_win_b_id"),
                    dbc.Input(
                        type="number",
                        id="area_win_b_id",
                        placeholder="Window area facing east",
                    ),
                ]
            ),
        width=3),
        dbc.Col(
            dbc.FormGroup(
                [
                    dbc.Label("South", html_for="area_win_c_id"),
                    dbc.Input(
                        type="number",
                        id="area_win_c_id",
                        placeholder="Window area facing south",
                    ),
                ]
            ),
        width=3),
        dbc.Col(
            dbc.FormGroup(
                [
                    dbc.Label("West", html_for="area_win_d_id"),
                    dbc.Input(
                        type="number",
                        id="area_win_d_id",
                        placeholder="Window area facing west",
                    ),
                ]
            ),
        width=3),
    ]),
    ],
)

output = html.Div("", id = "geometry_output_id")

content= html.Div([input, output])

layout = create_layout("geometry","/floorplan", "Enter your building dimensions", "/materials", content)