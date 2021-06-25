import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from app import app

from views.templates.header import navbar
from views.templates.footer import footer

# VIEW

content = dbc.Jumbotron(
    [
        html.H1("Welcome to REhome", className="display-3"),
        html.P(
            "An awesome webapp that lets you explore the carbondioxide emissions of buildings.",
            className="lead",
        ),
        html.Hr(className="my-2"),
        html.P(dbc.Button("START", color="primary", href="views/location_view"), className="lead"),
    ], style={"margin-bottom":"0rem","padding-bottom":"10rem"}
)

layout = html.Div(children=[
    navbar,
    content,
    footer,
])

if __name__ == '__main__':
    app.run_server(debug=True)