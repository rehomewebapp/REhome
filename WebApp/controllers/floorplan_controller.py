from dash.dependencies import Input, Output, State
from app import app
from models.building import location


@app.callback(
    Output('floorplan_map','center'),
    Output('floorplan_map','zoom'),
    Input('floorplan_heading','n_clicks'),
)
def set_latlng(n_clicks):
    #print('hello from set_latlng')
    loc = location.read_location_data()
    center = [float(loc['latitude']),float(loc['longitude'])]
    zoom = 13
    return center, zoom

if __name__ == '__main__':
    app.run_server(debug=True)