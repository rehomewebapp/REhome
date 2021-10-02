import dash_html_components as html
import dash_bootstrap_components as dbc


content = html.Div([
    #dbc.Button("Update", color="primary", id="update_weather_button_id"),
    html.Div(id = "weatherGraph_content_id"),
])