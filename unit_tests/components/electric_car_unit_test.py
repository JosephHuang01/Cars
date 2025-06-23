import unittest

from components.car import *
from components.battery import Battery
from components.electric_car import ElectricCar

class TestElectricCar(unittest.TestCase):
    # def test_default_capacity(self):
    #     # Arrange
    #     test_battery_charge_1 = ElectricCar('Tesla', 'S6', 2024, 70)

    #     # Act
    #     test_battery_charge_1.drive(Direction.LEFT, 25)

    #     # Assert
    #     self.assertEqual(test_battery_charge_1.battery.capacity_left, 65)
    #     self.assertAlmostEqual(test_battery_charge_1.battery.life, 92.857, places=3)

    #     # Arrange
    #     test_battery_charge_1.recharge_battery(5)

    #     # Assert
    #     self.assertEqual(test_battery_charge_1.battery.capacity, 70)

    #     # Act
    #     test_battery_charge_1.drive(Direction.FORWARD, 200)

    #     # Assert
    #     self.assertEqual(test_battery_charge_1.battery.capacity_left, 30)
    #     self.assertAlmostEqual(test_battery_charge_1.battery.life, 42.857, places=3)

    #     # Act
    #     test_battery_charge_1.drive(Direction.RIGHT, 100)

    #     # Assert
    #     self.assertEqual(test_battery_charge_1.battery.capacity_left, 10)
    #     self.assertAlmostEqual(test_battery_charge_1.battery.life, 14.2857, places=4)
    
    def test_drive_right_35(self):
        # Arrange
        test_my_electric_car_1 = ElectricCar('Tesla', 'S6', 2024)

        # Act
        test_my_electric_car_1.replace_battery(Battery(70, 0.2))
        test_my_electric_car_1.drive(DrivingDirection.RIGHT, 35)

        # Assert
        self.assertEqual(test_my_electric_car_1.miles_drove, 35)
        self.assertEqual(test_my_electric_car_1.battery.capacity_left, 63)
        self.assertEqual(test_my_electric_car_1.battery.life, 90)
        self.assertEqual(test_my_electric_car_1.direction, DrivingDirection.RIGHT)
    
    def test_drive_right_35_then_drive_back_140(self):
        # Arrange
        test_my_electric_car_1 = ElectricCar('Tesla', 'S6', 2024)
        test_my_electric_car_1.replace_battery(Battery(70, 0.2))
        test_my_electric_car_1.drive(DrivingDirection.RIGHT, 35)

        # Act
        test_my_electric_car_1.drive(DrivingDirection.BACKWARD, 140)

        # Assert
        self.assertEqual(test_my_electric_car_1.miles_drove, 175)
        self.assertEqual(test_my_electric_car_1.battery.capacity_left, 35)
        self.assertEqual(test_my_electric_car_1.battery.life, 50)
        self.assertEqual(test_my_electric_car_1.direction, DrivingDirection.BACKWARD)
    
    def test_drive_reverse_direction(self):
        # Arrange
        test_my_electric_car_1 = ElectricCar('Tesla', 'S6', 2024)
        test_my_electric_car_1.replace_battery(Battery(70, 0.2))
        test_my_electric_car_1.drive(DrivingDirection.RIGHT, 35)
        test_my_electric_car_1.drive(DrivingDirection.BACKWARD, 140)

        # Act
        test_my_electric_car_1.drive(DrivingDirection.LEFT, 35)

        # Assert
        self.assertEqual(test_my_electric_car_1.miles_drove, 210)
        self.assertEqual(test_my_electric_car_1.battery.capacity_left, 28)
        self.assertEqual(test_my_electric_car_1.battery.life, 40)
        self.assertEqual(test_my_electric_car_1.direction, DrivingDirection.LEFT)
    
    def test_drive_complete_circle(self):
        # Arrange
        test_my_electric_car_1 = ElectricCar('Tesla', 'S6', 2024)
        test_my_electric_car_1.replace_battery(Battery(70, 0.2))
        test_my_electric_car_1.drive(DrivingDirection.RIGHT, 35)
        test_my_electric_car_1.drive(DrivingDirection.BACKWARD, 140)
        test_my_electric_car_1.drive(DrivingDirection.LEFT, 35)

        # Act
        test_my_electric_car_1.drive(DrivingDirection.FORWARD, 140)
        
        # Assert
        self.assertEqual(test_my_electric_car_1.miles_drove, 350)
        self.assertEqual(test_my_electric_car_1.battery.capacity_left, 0)
        self.assertEqual(test_my_electric_car_1.battery.life, 0)
        self.assertEqual(test_my_electric_car_1.direction, DrivingDirection.FORWARD)
    
    def test_drive_complete_circle_and_add_name(self):
        # Arrange
        test_my_electric_car_1 = ElectricCar('Tesla', 'S6', 2024)
        test_my_electric_car_1.replace_battery(Battery(70, 0.2))
        test_my_electric_car_1.drive(DrivingDirection.RIGHT, 35)
        test_my_electric_car_1.drive(DrivingDirection.BACKWARD, 140)
        test_my_electric_car_1.drive(DrivingDirection.LEFT, 35)
        test_my_electric_car_1.assigned_driver("Amy")

        # Act
        test_my_electric_car_1.drive(DrivingDirection.FORWARD, 140)
        
        # Assert
        self.assertEqual(test_my_electric_car_1.miles_drove, 350)
        self.assertEqual(test_my_electric_car_1.battery.capacity_left, 0)
        self.assertEqual(test_my_electric_car_1.battery.life, 0)
        self.assertEqual(test_my_electric_car_1.direction, DrivingDirection.FORWARD)
        self.assertEqual(test_my_electric_car_1.driver.name, "Amy")
    
    def test_drive_complete_circle_add_name_and_seat_number(self):
        # Arrange
        test_my_electric_car_1 = ElectricCar('Tesla', 'S6', 2024)
        test_my_electric_car_1.replace_battery(Battery(70, 0.2))
        test_my_electric_car_1.drive(DrivingDirection.RIGHT, 35)
        test_my_electric_car_1.drive(DrivingDirection.BACKWARD, 140)
        test_my_electric_car_1.drive(DrivingDirection.LEFT, 35)
        test_my_electric_car_1.assigned_driver("Amy")
        test_my_electric_car_1.seat_number(4)

        # Act
        test_my_electric_car_1.drive(DrivingDirection.FORWARD, 140)
        
        # Assert
        self.assertEqual(test_my_electric_car_1.miles_drove, 350)
        self.assertEqual(test_my_electric_car_1.battery.capacity_left, 0)
        self.assertEqual(test_my_electric_car_1.battery.life, 0)
        self.assertEqual(test_my_electric_car_1.direction, DrivingDirection.FORWARD)
        self.assertEqual(test_my_electric_car_1.driver.name, "Amy")
        self.assertEqual(test_my_electric_car_1.seat.number, 4)
    
    def test_drive_complete_circle_add_name_seat_number_and_passenger(self):
        # Arrange
        test_my_electric_car_1 = ElectricCar('Tesla', 'S6', 2024)
        test_my_electric_car_1.replace_battery(Battery(70, 0.2))
        test_my_electric_car_1.drive(DrivingDirection.RIGHT, 35)
        test_my_electric_car_1.drive(DrivingDirection.BACKWARD, 140)
        test_my_electric_car_1.drive(DrivingDirection.LEFT, 35)
        test_my_electric_car_1.assigned_driver("Amy")
        test_my_electric_car_1.seat_number(4)
        test_my_electric_car_1.add_passenger("Elena")

        # Act
        test_my_electric_car_1.drive(DrivingDirection.FORWARD, 140)
        
        # Assert
        self.assertEqual(test_my_electric_car_1.miles_drove, 350)
        self.assertEqual(test_my_electric_car_1.battery.capacity_left, 0)
        self.assertEqual(test_my_electric_car_1.battery.life, 0)
        self.assertEqual(test_my_electric_car_1.direction, DrivingDirection.FORWARD)
        self.assertEqual(test_my_electric_car_1.driver.name, "Amy")
        self.assertEqual(test_my_electric_car_1.seat.number, 4)
        self.assertEqual(test_my_electric_car_1.passenger.name, "Elena")
    
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