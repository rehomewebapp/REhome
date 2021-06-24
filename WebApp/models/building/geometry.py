"""
The geometry module is used to create and manipulate the 
geometry of a building. Output should consist of all opaque and transparent
areas, their types (roof, outside_wall, window) and their orientations.
"""

from pyproj import Geod

def floorplane_from_geopolygone(polygone):
    """Calculate the area of a geopolygone.
    """
    # split polygone into list with lats and lons
    lats , lons = map(list, zip(*polygone))
    geod = Geod(ellps="WGS84")
    area = geod.polygon_area_perimeter(lons,lats)[0]

    return round(abs(area),2)

class Geometry():
    def __init__(self, width, length, story_height, stories, roof_type):
        self.width = width
        self.length = length
        self. story_height = story_height
        self.stories = stories
        self.roof_type = roof_type
        self.floor_area = self._floorplane_from_width_and_length()
        self.volume = width * length * story_height * stories

    def _floorplane_from_width_and_length(self):
        """ Calculate the area and create a list of all floor lines
        """
        area = self.width * self.length
        return area



    def _walls_from_floor_and_stories(floor : float,
                                story_height: float,
                                story_n: int):
        pass

    def rotate_building():
        pass
