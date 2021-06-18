import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app, server
from views import home_view  ,location_view
from controllers import location_controller


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
        return home_view.layout
    elif pathname == '/views/location_view':
        return location_view.layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)