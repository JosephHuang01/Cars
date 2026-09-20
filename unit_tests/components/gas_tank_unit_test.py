import unittest

from components.gas_tank import GasTank

class TestGasTank(unittest.TestCase):

    def test_default_capacity(self):
        test_gas_tank_1 = GasTank(15, 0.05)
        test_gas_tank_1.travel_distance(0)
        self.assertEqual(test_gas_tank_1.capacity_left, 15)
        self.assertEqual(test_gas_tank_1.percentage, 100)
    
    def test_driving_at_half_full_tank(self):
        test_gas_tank_3 = GasTank(15, 0.05)
        test_gas_tank_3.travel_distance(150)
        self.assertEqual(test_gas_tank_3.capacity_left, 7.5)
        self.assertEqual(test_gas_tank_3.percentage, 50)
    
    def test_refuel(self):
        test_gas_tank_5 = GasTank(15, 0.05)
        test_gas_tank_5.travel_distance(300)
        self.assertEqual(test_gas_tank_5.capacity_left, 0)
        self.assertEqual(test_gas_tank_5.percentage, 0)

    def test_driving_five_times(self):
        test_gas_tank_3 = GasTank(15, 0.05)
        test_gas_tank_3.travel_distance(75)
        self.assertEqual(test_gas_tank_3.capacity_left, 11.25)
        self.assertEqual(test_gas_tank_3.percentage, 75)
        test_gas_tank_3.travel_distance(50)
        self.assertEqual(test_gas_tank_3.capacity_left, 8.75)
        #self.assertEqual(test_gas_tank_3.percentage, 58.333333333333336)
        self.assertAlmostEqual(test_gas_tank_3.percentage, 58.33333, places=5)
        test_gas_tank_3.travel_distance(75)
        self.assertEqual(test_gas_tank_3.capacity_left, 5)
        self.assertAlmostEqual(test_gas_tank_3.percentage, 33.33333, places=5)
        test_gas_tank_3.travel_distance(60)
        self.assertEqual(test_gas_tank_3.capacity_left, 2)
        self.assertAlmostEqual(test_gas_tank_3.percentage, 13.33333, places=5)
        test_gas_tank_3.travel_distance(25)
        self.assertEqual(test_gas_tank_3.capacity_left, 0.75)
        self.assertEqual(test_gas_tank_3.percentage, 5)
        test_gas_tank_3.travel_distance(15)
        self.assertEqual(test_gas_tank_3.capacity_left, 0)
        self.assertEqual(test_gas_tank_3.percentage, 0)
    
    def test_driving_twice_and_refill(self):
        test_gas_tank_3 = GasTank(15, 0.05)
        test_gas_tank_3.travel_distance(75)
        self.assertEqual(test_gas_tank_3.capacity_left, 11.25)
        self.assertEqual(test_gas_tank_3.percentage, 75)
        test_gas_tank_3.travel_distance(50)
        self.assertEqual(test_gas_tank_3.capacity_left, 8.75)
        #self.assertEqual(test_gas_tank_3.percentage, 58.333333333333336)
        self.assertAlmostEqual(test_gas_tank_3.percentage, 58.33333, places=5)
    
        test_gas_tank_3.fill_gas()
        test_gas_tank_3.travel_distance(75)
        self.assertEqual(test_gas_tank_3.capacity_left, 11.25)
        self.assertEqual(test_gas_tank_3.percentage, 75)
        test_gas_tank_3.travel_distance(60)
        self.assertEqual(test_gas_tank_3.capacity_left, 8.25)
        self.assertAlmostEqual(test_gas_tank_3.percentage, 55)
        test_gas_tank_3.travel_distance(25)
        self.assertEqual(test_gas_tank_3.capacity_left, 7)
        self.assertAlmostEqual(test_gas_tank_3.percentage, 46.66667, places=5)

        test_gas_tank_3.fill_gas()
        test_gas_tank_3.travel_distance(15)
        self.assertEqual(test_gas_tank_3.capacity_left, 14.25)
        self.assertEqual(test_gas_tank_3.percentage, 95)

unittest.main()