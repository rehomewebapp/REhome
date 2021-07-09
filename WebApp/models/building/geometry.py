"""
The geometry module is used to create and manipulate the 
geometry of a building. Output should consist of all opaque and transparent
areas, their types (roof, outside_wall, window) and their orientations.
"""

from pyproj import Geod
import csv

data_path = "WebApp/models/building/data/"

def floorplane_from_geopolygone(polygone):
    """Calculate the area of a geopolygone.
    """
    # split polygone into list with lats and lons
    lats , lons = map(list, zip(*polygone))
    geod = Geod(ellps="WGS84")
    area = geod.polygon_area_perimeter(lons,lats)[0]

    return round(abs(area),2)

def perimeter_from_geopolygone(polygone):
    """Calculate the perimeter of a geopolygone.
    """
    # split polygone into list with lats and lons
    lats , lons = map(list, zip(*polygone))
    geod = Geod(ellps="WGS84")
    perimeter = geod.polygon_area_perimeter(lons,lats)[1]

    return round(abs(perimeter),2)

def facade_area(perimeter, height):
    area = perimeter * height
    return area

def height_from_story(n_story, story_height):
    height = n_story * story_height
    return height

def save_geometry_data(perimeter, area):
    """
    save the perimeter of the building in a csv file in the building models
    data directory.
    """
    geometry = {'perimeter':perimeter, 'area':area}
    with open(data_path + "userid_geometry.csv", 'w') as csvfile:
        fieldnames = ['perimeter', 'groundArea']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(geometry)

def read_geometry_data(filename):

    """Load the geometry data from a csv file.

    Parameters
    ----------
    filename : string
        filename of the csv file containing the geometry data

    Returns
    -------
    dict containing
        - groundArea (float): Ground area of the building [m^2]
        - perimeter (float): Perimeter of the building [m]
    """

    with open(data_path + filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            geometry = row
    return geometry

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
