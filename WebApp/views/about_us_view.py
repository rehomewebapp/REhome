import dash
import dash_html_components as html
import dash_core_components as dcc

from views.templates.footer import footer
from views.templates.header import create_navbar

# every child page has a layout as shown below and can be run via the code index.py 
# https://dash.plotly.com/introduction please go through this link to add more features in these cases

navbar = create_navbar("About Us")
ABOUT_US = "/assets/about_us.png"

layout = html.Div(children=[
    navbar,
    html.Br(),
    html.P("We are a team of students who want to save the world."),
    html.Img(src=ABOUT_US),
    footer,
])
