import unittest

from components.electric_car import ElectricCar

class TestElectricCar(unittest.TestCase):
    def test_default_capacity(self):
        # Arrange
        test_battery_charge_1 = ElectricCar('Tesla', 'S6', 2024, 70)

        # Act
        test_battery_charge_1.travel_distance(25)

        # Assert
        self.assertEqual(test_battery_charge_1.capacity_left, 65)
        self.assertAlmostEqual(test_battery_charge_1.life, 92.857, places=3)

        # Arrange
        test_battery_charge_1.recharge_battery(5)

        # Assert
        self.assertEqual(test_battery_charge_1.capacity, 70)

        # Act
        test_battery_charge_1.travel_distance(200)

        # Assert
        self.assertEqual(test_battery_charge_1.capacity_left, 30)
        self.assertAlmostEqual(test_battery_charge_1.life, 42.857, places=3)

        # Act
        test_battery_charge_1.travel_distance(100)

        # Assert
        self.assertEqual(test_battery_charge_1.capacity_left, 10)
        self.assertAlmostEqual(test_battery_charge_1.life, 14.2857, places=4)
    
    # def test_half_capacity(self):
    #     test_batter_charge_3 = ElectricCar('Subaru', 'Outback', 2023, 35)
    #     test_batter_charge_3.turn_right(8)
    #     self.assertEqual(test_batter_charge_3.read_odometer(), 8)

    # def test_recharge(self):
    #     test_battery_charge_5 = ElectricCar('BMW', 'iX', 2022, 85)
    #     test_battery_charge_5.drive_backward(4)
    #     test_battery_charge_5.turn_left(4)
    #     self.assertEqual(test_battery_charge_5.read_odometer(), 8)

unittest.main()