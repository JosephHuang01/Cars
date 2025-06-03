import unittest

from components.car import Car, Position
from components.gas_car import GasCar
from components.gas_tank import GasTank

class TestGasCar(unittest.TestCase):

    def test_default_capacity(self):
        test_gas_tank_1 = GasCar('Toyota', 'Corolla', 2017)
        test_gas_tank_1.move_with_gas(15, "foward", 3)
        test_gas_tank_1.drive_forward(1)
        test_gas_tank_1.turn_right(2)
        self.assertEqual(test_gas_tank_1.read_odometer(), 3)
    
    def test_driving_with_tank_half_full(self):
        test_gas_tank_3 = GasCar('Hyundai', 'Kona', 2023)
        test_gas_tank_3.move_with_gas(5, "left", 4)
        test_gas_tank_3.turn_left(4)
        self.assertEqual(test_gas_tank_3.read_odometer(), 4)

    def test_refuel(self):
        test_gas_tank_5 = GasCar('Honda', 'Civic', 2020)
        test_gas_tank_5.move_with_gas(10, "backward", 10)
        test_gas_tank_5.drive_backward(6)
        test_gas_tank_5.turn_left(4)
        self.assertEqual(test_gas_tank_5.read_odometer(), 10)

if __name__ == '__main__':
    unittest.main()