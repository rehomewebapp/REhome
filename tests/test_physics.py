import unittest
from WebApp.models.building import physics

class TestBuildingPhysics(unittest.TestCase):
    def test_transmission(self):
        self.assertEqual(physics.transmission(uValue=2,area=5,tempIn=20,tempAmb=10),100)

    def test_solarGains(self):
        self.assertEqual(physics.solarGains(gValue=2,area=5,irrad=1000),10000)

    def test_infAndVent(self):
        self.assertEqual(physics.infAndVent(n=0.5,volume=3600,tempIn=20,tempAmb=10),6875)

    def test_heatDemand(self):
        self.assertEqual(physics.heatDemand(gains=[10,100], losses=[10,100]),0)

    def test_heatDemandWithEmptyList(self):
        self.assertEqual(physics.heatDemand(gains=[10,100]),-110)

    def test_heatflow2Energy(self):
        self.assertEqual(physics.heatflow2Energy(heatflow=10,timestep=1),10)

if __name__ == '__main__':
    unittest.main()