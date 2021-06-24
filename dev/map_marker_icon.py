import dash
import dash_html_components as html
import dash_leaflet as dl

# Setup icon options, example from Leaflet doc (https://leafletjs.com/examples/custom-icons/).
icon = {
    "iconUrl": '/assets/map-marker-radius.png',
    "shadowUrl": 'https://leafletjs.com/examples/custom-icons/leaf-shadow.png',
    "iconSize": [48, 48],  # size of the icon
    "shadowSize": [50, 64],  # size of the shadow
    "iconAnchor": [22, 94],  # point of the icon which will correspond to marker's location
    "shadowAnchor": [4, 62],  # the same for the shadow
    "popupAnchor": [-3, -76]  # point from which the popup should open relative to the iconAnchor
}
# Create example app.
app = dash.Dash()
app.layout = html.Div([
    dl.Map([dl.TileLayer(), dl.Marker(position=(56, 10), icon=icon)],
           id="map", style={'width': '100%', 'height': '50vh', 'margin': "auto", "display": "block"}),
])

if __name__ == '__main__':
    app.run_server()