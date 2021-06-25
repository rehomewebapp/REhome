import dash
import dash_html_components as html
import dash_core_components as dcc

from app import app

from views.templates.header import navbar

# VIEW

layout = html.Div(children=[
    navbar,
    html.H1(children='Welcome to REhome'),

    html.Div(children='''
        An awesome webapp that lets you explore the carbondioxide emissions of buildings.
    '''),
    dcc.Link('Location', href="/views/location_view"),
    html.Br(),
    dcc.Link('About Us', href="/views/about_us_view")
])

if __name__ == '__main__':
    app.run_server(debug=True)