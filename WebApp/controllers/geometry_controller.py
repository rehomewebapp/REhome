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
    Output("area_win_a_id", "value"),
    Output("area_win_b_id", "value"),
    Output("area_win_c_id", "value"),
    Output("area_win_d_id", "value"),
    Input("n_storys_id", "value"),
    Input("story_height_id", "value"),
    Input("area_win_a_id", "value"),
    Input("area_win_b_id", "value"),
    Input("area_win_c_id", "value"),
    Input("area_win_d_id", "value"),
    Input("geometry_done_button_id", "n_clicks"),
)
def inputDone(n_storys, story_height, area_win_a,area_win_b,area_win_c, area_win_d, clicks):
    ctx = callback_context
    # check which input has triggered the callback
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    # on pageload: fill input fields with building data
    if not ctx.triggered:
        building = read_building_data_yaml("userID")
        n_storys = building['nStorys']
        story_height = building['thZones']['livingSpace']['storyHeight']
        area_win_a = building['thZones']['livingSpace']['transPlanes']['windowA']['area']
        area_win_b = building['thZones']['livingSpace']['transPlanes']['windowB']['area']
        area_win_c = building['thZones']['livingSpace']['transPlanes']['windowC']['area']
        area_win_d = building['thZones']['livingSpace']['transPlanes']['windowD']['area']
        return False, "success", n_storys, story_height, area_win_a, area_win_b, area_win_c, area_win_d

    # disable button if one input field is empty
    if not n_storys or not story_height or not area_win_a or not area_win_b or not area_win_c or not area_win_d:
        return True, "primary", n_storys, story_height, area_win_a, area_win_b, area_win_c, area_win_d

    # save building data on button click
    if button_id == "geometry_done_button_id":
        # calculate geometry values
        height = geometry.height_from_story(n_storys, story_height)

        building = read_building_data_yaml(userID='userID')
        perimeter = building['perimeter']
        groundArea = building['groundArea']

        heatedArea = groundArea * n_storys
        volume = groundArea * height
        facadearea = geometry.facade_area(perimeter, height) - sum([area_win_a, area_win_b, area_win_c, area_win_d])


        building['nStorys'] = n_storys
        building['thZones']['livingSpace']['storyHeight'] = story_height
        building['thZones']['livingSpace']['opaquePlanes']['facade']['area'] = facadearea
        building['thZones']['livingSpace']['opaquePlanes']['roof']['area'] = groundArea
        building['thZones']['livingSpace']['opaquePlanes']['floor']['area'] = groundArea
        building['thZones']['livingSpace']['floorArea'] = heatedArea
        building['thZones']['livingSpace']['volume'] = volume
        building['thZones']['livingSpace']['transPlanes']['windowA']['area'] = area_win_a
        building['thZones']['livingSpace']['transPlanes']['windowB']['area'] = area_win_b
        building['thZones']['livingSpace']['transPlanes']['windowC']['area'] = area_win_c
        building['thZones']['livingSpace']['transPlanes']['windowD']['area'] = area_win_d
        save_building_data_yaml(building)

        return False, "success", n_storys, story_height, area_win_a, area_win_b, area_win_c, area_win_d

    # activate button if all inputs are filled
    else:
        return False, "primary", n_storys, story_height, area_win_a, area_win_b, area_win_c, area_win_d


    