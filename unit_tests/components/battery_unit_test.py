import unittest

# This works!!!
# python unit_tests/battery_unit_test.py

# This works as well!!!
# python -m unit_tests.battery_unit_test

# python -m unit_tests.components.battery_unit_test


# from ..components.battery import Battery
# car_1 = Battery.traveled_distance(25)

import sys

sys.path.insert(0, r'C:\Users\kungf\OneDrive\Documents\Source\Cars\components')

from battery import Battery

class TestBattery(unittest.TestCase):

    def test_default_capacity(self):
        battery_1 = Battery()
        battery_1.travel_distance(0)
        self.assertEqual(battery_1.capacity, 50)
        self.assertEqual(battery_1.life, 100)
    
    def test_driving_large_capacity(self):
        battery_2 = Battery()
        battery_2.travel_distance(25)
        self.assertEqual(battery_2.capacity, 45)
        self.assertEqual(battery_2.life, 90)
    
    def test_driving_half_capacity(self):
        battery_3 = Battery()
        battery_3.travel_distance(125)
        self.assertEqual(battery_3.capacity, 25)
        self.assertEqual(battery_3.life, 50)
    
    def test_driving_low_capacity(self):
        battery_4 = Battery()
        battery_4.travel_distance(225)
        self.assertEqual(battery_4.capacity, 5)
        self.assertEqual(battery_4.life, 10)
    
    def test_recharge(self):
        battery_5 = Battery()
        battery_5.travel_distance(250)
        self.assertEqual(battery_5.capacity, 0)
        self.assertEqual(battery_5.life, 0)

unittest.main()
#battery_1 = Battery.traveled_distance(25)