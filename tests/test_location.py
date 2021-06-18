import unittest
from WebApp.models.building import location

class TestLocation(unittest.TestCase):
    def test_conv_zip_to_location(self):
        self.assertEqual(location.conv_zip_to_location(79271)['city'], 'Sankt Peter')

if __name__ == '__main__':
    unittest.main()