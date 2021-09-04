from dash.dependencies import Input, Output
from app import app
from models.building import geometry
from dash.exceptions import PreventUpdate
from models.building.buildingFactory import read_building_data_yaml, save_building_data_yaml



@app.callback(
    Output("geometry_output_id","children"),
    Output('geometry_done_button_id', 'disabled'), 
    Output('geometry_done_button_id', 'color'),
    Output("n_storys_id", "value"),
    Output("story_height_id", "value"),
    Input("n_storys_id", "value"),
    Input("story_height_id", "value")
)
def handle_facade(n_storys, story_height):
    building = read_building_data_yaml("userID")
    if n_storys == None and story_height == None:
        n_storys = building['nStorys']
        story_height = building['thZones']['livingSpace']['storyHeight']
        return "", False, "success", n_storys, story_height

    #if only one parameter is given
    if n_storys == None or story_height == None:
        return "", True, "primary", n_storys, story_height

    height = geometry.height_from_story(n_storys, story_height)

    building = read_building_data_yaml(userID='userID')
    perimeter = building['perimeter']
    groundArea = building['groundArea']
    
    heatedArea = groundArea * n_storys
    volume = groundArea * height
    facadearea = geometry.facade_area(perimeter, height)

    # TODO! calculate window area and subtract from facade area
    building['thZones']['livingSpace']['opaquePlanes']['facade']['area'] = facadearea
    building['thZones']['livingSpace']['opaquePlanes']['roof']['area'] = groundArea
    building['thZones']['livingSpace']['opaquePlanes']['floor']['area'] = groundArea
    building['thZones']['livingSpace']['floorArea'] = heatedArea
    building['thZones']['livingSpace']['volume'] = volume
    save_building_data_yaml(building)

    return f'{height=}, {perimeter=}, {facadearea=}', False, "success", n_storys, story_height