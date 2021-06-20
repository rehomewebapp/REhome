import dash
import dash_html_components as html
import dash_core_components as dcc

layout = html.Div(children=[
    html.H1(children="About Us"),
    html.Br(),
    dcc.Link('Home', href="/"),
])