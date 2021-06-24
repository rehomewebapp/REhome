import dash_html_components as html
import dash_leaflet as dl
from dash import Dash

app = Dash()
app.layout = html.Div([
    dl.Map([dl.TileLayer(maxZoom = 21, maxNativeZoom = 19),
            dl.MeasureControl(position="topleft", primaryLengthUnit="meters", primaryAreaUnit="sqmeters",
                              activeColor="#214097", completedColor="#972158")],
           style={'width': '100%', 'height': '50vh', 'margin': "auto", "display": "block"}),
])

if __name__ == '__main__':
    app.run_server()