from dash.dependencies import Input, Output
from app import app
from models.building import geometry
from dash.exceptions import PreventUpdate


@app.callback(
    Output("geometry_output_id","children"),
    Input("n_storys_id", "value"),
    Input("story_height_id", "value")
)
def handle_facade(n_storys, story_height):
    if n_storys == None or story_height == None:
        raise PreventUpdate()
    height = geometry.height_from_story(n_storys, story_height)
    geometry_dict = geometry.read_geometry_data()
    perimeter = float(geometry_dict['perimeter'])
    floorarea = float(geometry_dict['area'])
    facadearea = geometry.facade_area(perimeter, height)
    return f'{height=}, {perimeter=}, {floorarea=}, {facadearea=}'