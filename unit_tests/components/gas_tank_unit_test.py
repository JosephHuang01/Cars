import unittest

from components.gas_tank import GasTank

class TestGasTank(unittest.TestCase):

    def test_default_capacity(self):
        test_gas_tank_1 = GasTank()
        test_gas_tank_1.travel_distance(0)
        self.assertEqual(test_gas_tank_1.capacity, 15)
        self.assertEqual(test_gas_tank_1.life, 100)
    
    def test_driving_at_half_full_tank(self):
        test_gas_tank_3 = GasTank()
        test_gas_tank_3.travel_distance(150)
        self.assertEqual(test_gas_tank_3.capacity, 7.5)
        self.assertEqual(test_gas_tank_3.life, 50)
    
    def test_refuel(self):
        test_gas_tank_5 = GasTank()
        test_gas_tank_5.travel_distance(300)
        self.assertEqual(test_gas_tank_5.capacity, 0)
        self.assertEqual(test_gas_tank_5.life, 0)

unittest.main()