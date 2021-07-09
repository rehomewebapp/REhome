import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app, server
from views import home_view  ,location_view, about_us_view, floorplan_view, geometry_view, materials_view
from controllers import home_controller, location_controller, floorplan_controller, geometry_controller, materials_controller

# this sets the layout of our webpage, dcc.location sets the url of the page, 
# and html.div returns the page content of all the child pages of our web app
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# the callback display_page receives the current pathname (the last part of the URL) of the page. 
# The callback simply displays the pathname on page but it could use the pathname to display different content.

@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))

# the below function, returns the layout of all the different views, they also have to be imported in line 6.
def display_page(pathname):
    if pathname == '/':
        return home_view.layout
    elif pathname == '/location':
        return location_view.layout
    elif pathname == '/about_us':
        return about_us_view.layout
    elif pathname == '/floorplan':
        return floorplan_view.layout
    elif pathname == '/geometry':
        return geometry_view.layout
    elif pathname == '/materials':
        return materials_view.layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)
