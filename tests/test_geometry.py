import unittest
from WebApp.models.building.geometry import Geometry

class TestGeometry(unittest.TestCase):
    def setUp(self):
        self.geometry = Geometry(width = 1, length = 2, story_height = 3, stories = 4, roof_type = "flat")

    def test_volume_calculation(self):
        self.assertEqual(self.geometry.volume, 24)

    def test_floorplan_area_calculation(self):
        self.assertEqual(self.geometry.floor_area, 2)
        pass

if __name__ == '__main__':
    unittest.main()