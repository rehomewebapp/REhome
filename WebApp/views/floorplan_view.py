import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_leaflet as dl

from app import app

# VIEW

layout = html.Div(children=[
    html.H1(children='Floorplan', id = 'floorplan_heading'),
    html.H2(children='Locate your home on the map and trace the outline.'),
    dl.Map(id = "floorplan_map",
        children=[
                dl.TileLayer(maxZoom = 21, maxNativeZoom = 19), # 
                dl.MeasureControl(
                    position="topleft", 
                    primaryLengthUnit="meters", 
                    primaryAreaUnit="sqmeters", 
                    activeColor="#214097", 
                    completedColor="#972158")],
        style={'width': '1000px', 'height': '500px'}
    ),
    dcc.Link('Home', href="/"), # link to landing page
])

if __name__ == '__main__':
    app.run_server(debug=True)