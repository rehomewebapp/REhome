"""
The geometry module is used to create and manipulate the 
geometry of a building. Output should consist of all opaque and transparent
areas, their types (roof, outside_wall, window) and their orientations.
"""

from pyproj import Geod
import csv

data_path = "WebApp/models/building/data/"

def area_from_geopolygone(polygone):
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




