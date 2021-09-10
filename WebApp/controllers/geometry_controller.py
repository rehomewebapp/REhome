from app import app
from dash.dependencies import Input, Output
from dash import callback_context

from models.building import geometry
from models.building.buildingFactory import read_building_data_yaml, save_building_data_yaml



@app.callback(
    Output('geometry_done_button_id', 'disabled'), 
    Output('geometry_done_button_id', 'color'),
    Output("n_storys_id", "value"),
    Output("story_height_id", "value"),
    Input("n_storys_id", "value"),
    Input("story_height_id", "value"),
    Input("geometry_done_button_id", "n_clicks"),
)
def inputDone(n_storys, story_height, clicks):
    ctx = callback_context
    # check which input has triggered the callback
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    # on pageload: fill input fields with building data
    if not ctx.triggered:
        building = read_building_data_yaml("userID")
        n_storys = building['nStorys']
        story_height = building['thZones']['livingSpace']['storyHeight']
        return False, "success", n_storys, story_height

    # disable button if one input field is empty
    if n_storys == None or story_height == None:
        return True, "primary", n_storys, story_height

    # save building data on button click
    if button_id == "geometry_done_button_id":
        # calculate geometry values
        height = geometry.height_from_story(n_storys, story_height)

        building = read_building_data_yaml(userID='userID')
        perimeter = building['perimeter']
        groundArea = building['groundArea']
        
        heatedArea = groundArea * n_storys
        volume = groundArea * height
        facadearea = geometry.facade_area(perimeter, height)

        # TODO! calculate window area and subtract from facade area
        building['nStorys'] = n_storys
        building['thZones']['livingSpace']['storyHeight'] = story_height
        building['thZones']['livingSpace']['opaquePlanes']['facade']['area'] = facadearea
        building['thZones']['livingSpace']['opaquePlanes']['roof']['area'] = groundArea
        building['thZones']['livingSpace']['opaquePlanes']['floor']['area'] = groundArea
        building['thZones']['livingSpace']['floorArea'] = heatedArea
        building['thZones']['livingSpace']['volume'] = volume
        save_building_data_yaml(building)

        return False, "success", n_storys, story_height

    # activate button if all inputs are filled
    else:
        return False, "primary", n_storys, story_height


    