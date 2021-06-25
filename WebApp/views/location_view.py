import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from views.templates.header import navbar
#from dash_html_components.Button import Button

from app import app

# VIEW

layout = html.Div(children=[
    navbar,
    html.H1(children='Choose Location'),

    html.Div(children='''
        Please enter your post code.
    '''),
    dcc.Input(id="input", type="text", placeholder="Enter post code", value = ''),
    dbc.Button("Submit", id="submit_button", className='',  n_clicks=0),
    html.Div(id='location_output',children=''),
    dcc.Link('Next',id="link_to_floorplan", href="/floorplan"),
    html.Br(),
    
    
])

if __name__ == '__main__':
    app.run_server(debug=True)