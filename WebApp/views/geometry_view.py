import dash_html_components as html
import dash_bootstrap_components as dbc

from views.templates.createLayout import create_layout


input = html.Div(
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
        ),
        dbc.Col(
            dbc.FormGroup(
                [
                    dbc.Label("Height of the storys [m]", html_for="story_height_id"),
                    dbc.Input(
                        type="number",
                        step=0.01,
                        id="story_height_id",
                        placeholder="Enter height of the storys",
                    ),
                ]
            ),
        ),
    ],
)

output = html.Div("", id = "geometry_output_id")

content= html.Div([input, output])

layout = create_layout("geometry","/floorplan", "Enter your building dimensions", "/materials", content)