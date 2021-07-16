from dash.dependencies import Input, Output
from app import app
from models.building import geometry
from dash.exceptions import PreventUpdate
from models.building.buildingFactory import read_building_data, save_building_data


@app.callback(
    Output("geometry_output_id","children"),
    Output('geometry_done_button_id', 'disabled'), 
    Output('geometry_done_button_id', 'color'),
    Input("n_storys_id", "value"),
    Input("story_height_id", "value")
)
def handle_facade(n_storys, story_height):
    if n_storys == None or story_height == None:
        raise PreventUpdate()
    height = geometry.height_from_story(n_storys, story_height)
    #geometry_dict = geometry.read_geometry_data()
    building = read_building_data(userID='userID')
    perimeter = building['thZones']['tz0']['perimeter']
    facadearea = geometry.facade_area(perimeter, height)
    # TODO! calculate window area and subtract from facade area
    building['thZones']['tz0']['opaquePlanes'] = {'facade':{'area':facadearea}}
    save_building_data(building)

    return f'{height=}, {perimeter=}, {facadearea=}', False, "success"