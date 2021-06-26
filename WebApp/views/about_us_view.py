import dash
import dash_html_components as html
import dash_core_components as dcc
from views.templates.header import create_navbar

# every child page has a layout as shown below and can be run via the code index.py 
# https://dash.plotly.com/introduction please go through this link to add more features in these cases

navbar = create_navbar("About Us")

layout = html.Div(children=[
    navbar,
    html.H1(children="About Us"),

])
