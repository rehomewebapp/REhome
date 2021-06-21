import dash
import dash_html_components as html
import dash_core_components as dcc
# every child page has a layout as shown below and can be run via the code index.py 
# https://dash.plotly.com/introduction please go through this link to add more features in these cases
layout = html.Div(children=[
    html.H1(children="About Us"),
    html.Br(),
    dcc.Link('Home', href="/"),
])
