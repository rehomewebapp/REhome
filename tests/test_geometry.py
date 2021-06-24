import unittest
from WebApp.models.building.geometry import Geometry
from WebApp.models.building.geometry import floorplane_from_geopolygone

class TestGeometry(unittest.TestCase):
    def setUp(self):
        self.geometry = Geometry(width = 1, length = 2, story_height = 3, stories = 4, roof_type = "flat")

    def test_volume_calculation(self):
        self.assertEqual(self.geometry.volume, 24)

    def test_floorplan_area_calculation(self):
        self.assertEqual(self.geometry.floor_area, 2)
        pass

    def test_conv_geopolygone_to_area(self):
        polygone = [
            [48.00622801127556, 8.037822023034098],
            [48.00614860319703, 8.03798630833626],
            [48.00605663323576, 8.03785488009453],
            [48.00613200375274, 8.037684559822084],
        ]
        area = floorplane_from_geopolygone(polygone)
        self.assertEqual(area,320.61)

if __name__ == '__main__':
    unittest.main()