import unittest
from WebApp.models.building.geometry import Geometry
from WebApp.models.building.geometry import floorplane_from_geopolygone, perimeter_from_geopolygone, facade_area, height_from_story

class TestGeometry(unittest.TestCase):
    def setUp(self):
        self.geometry = Geometry(width = 1, length = 2, story_height = 3, stories = 4, roof_type = "flat")

    def test_volume_calculation(self):
        self.assertEqual(self.geometry.volume, 24)

    def test_floorplan_area_calculation(self):
        self.assertEqual(self.geometry.floor_area, 2)
        pass

    def test_conv_geopolygone_from_area(self):
        polygone = [
            [48.00622801127556, 8.037822023034098],
            [48.00614860319703, 8.03798630833626],
            [48.00605663323576, 8.03785488009453],
            [48.00613200375274, 8.037684559822084],
        ]
        area = floorplane_from_geopolygone(polygone)
        self.assertEqual(area,216.78)

    def test_conv_geopolygone_from_perimeter(self):
        polygone = [
            [48.00622801127556, 8.037822023034098],
            [48.00614860319703, 8.03798630833626],
            [48.00605663323576, 8.03785488009453],
            [48.00613200375274, 8.037684559822084],
        ]
        perimeter = perimeter_from_geopolygone(polygone)
        self.assertEqual(perimeter,59.3)

    def test_calc_facade_area(self):
        perimeter = 50 # m perimeter of the builiding
        height = 5     # m building height from ground, without roof
        area = facade_area(perimeter, height)
        self.assertEqual(area,250)

    def test_height_from_story(self):
        story_height = 5 # height of one story
        n_story = 2 # number of story
        height = height_from_story(n_story, story_height)
        self.assertEqual(height,10)



if __name__ == '__main__':
    unittest.main()