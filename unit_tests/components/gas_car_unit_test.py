import unittest

from components.car import *
from components.gas_tank import GasTank
from components.gas_car import GasCar


class TestGasCar(unittest.TestCase):

    def test_drive_forward_60(self):
        # Arrange
        test_my_gas_car_1 = GasCar('Toyota', 'Corolla', 2017)
        test_my_gas_car_1.add_gas_tank(GasTank(15, 0.05))

        # Act
        test_my_gas_car_1.drive(DrivingDirection.FORWARD, 60)

        # Assert
        self.assertEqual(test_my_gas_car_1.miles_drove, 60)
        self.assertEqual(test_my_gas_car_1.gas_tank.capacity_left, 12)
        self.assertEqual(test_my_gas_car_1.gas_tank.percentage, 80)
        self.assertEqual(test_my_gas_car_1.direction, DrivingDirection.FORWARD)
        #self.assertEqual(test_my_gas_car_1.coordinate_direction, CoordinateDirection.Y_PLUS)
        self.assertEqual(test_my_gas_car_1.position.y, 60)
        # todo: add position x y and x/y direction assert

    def test_coordinate_direction_after_drive_foward_60(self):
        # Arrange
        test_my_gas_car_1 = GasCar('Toyota', 'Corolla', 2017)
        test_my_gas_car_1.add_gas_tank(GasTank(15, 0.05))
       
        # Act
        test_my_gas_car_1.drive(DrivingDirection.FORWARD, 60)

        # Assert       
        self.assertEqual(test_my_gas_car_1.direction, DrivingDirection.FORWARD)     
        self.assertEqual(test_my_gas_car_1.set_present_coordinate_direction.current_coordinate_direction, CoordinateDirection.Y_PLUS)

    def test_coordinate_direction_after_turn_left_60_and_turn_left_60(self):
        # Arrange
        test_my_gas_car_1 = GasCar('Toyota', 'Corolla', 2017)
        test_my_gas_car_1.add_gas_tank(GasTank(15, 0.05))
        test_my_gas_car_1.drive(DrivingDirection.LEFT, 60)
       
        # Act
        test_my_gas_car_1.drive(DrivingDirection.LEFT, 60)

        # Assert       
        self.assertEqual(test_my_gas_car_1.direction, DrivingDirection.LEFT)
        self.assertEqual(test_my_gas_car_1.set_present_coordinate_direction.current_coordinate_direction, CoordinateDirection.X_MINUS)

    def test_coordinate_direction_after_drive_foward_60_then_turn_left_120(self):
        # Arrange
        test_my_gas_car_1 = GasCar('Toyota', 'Corolla', 2017)
        test_my_gas_car_1.add_gas_tank(GasTank(15, 0.05))
        test_my_gas_car_1.drive(DrivingDirection.FORWARD, 60)
       
        # Act
        test_my_gas_car_1.drive(DrivingDirection.LEFT, 120)

        # Assert
        self.assertEqual(test_my_gas_car_1.direction, DrivingDirection.LEFT)
        self.assertEqual(test_my_gas_car_1.set_present_coordinate_direction.current_coordinate_direction, CoordinateDirection.X_MINUS)

    def test_coordinate_direction_after_drive_foward_60_then_turn_right_120(self):
        # Arrange
        test_my_gas_car_1 = GasCar('Toyota', 'Corolla', 2017)
        test_my_gas_car_1.add_gas_tank(GasTank(15, 0.05))
        test_my_gas_car_1.drive(DrivingDirection.FORWARD, 60)
       
        # Act
        test_my_gas_car_1.drive(DrivingDirection.RIGHT, 120)

        # Assert       
        self.assertEqual(test_my_gas_car_1.direction, DrivingDirection.RIGHT)
        self.assertEqual(test_my_gas_car_1.set_present_coordinate_direction.current_coordinate_direction, CoordinateDirection.X_PLUS)    

    def test_drive_foward_60_then_turn_left_120(self):
        # Arrange
        test_my_gas_car_1 = GasCar('Toyota', 'Corolla', 2017)
        test_my_gas_car_1.add_gas_tank(GasTank(15, 0.05))
        test_my_gas_car_1.drive(DrivingDirection.FORWARD, 60)
       
        # Act
        test_my_gas_car_1.drive(DrivingDirection.LEFT, 60)

        # Assert
        self.assertEqual(test_my_gas_car_1.miles_drove, 120)
        self.assertEqual(test_my_gas_car_1.gas_tank.capacity_left, 9)
        self.assertEqual(test_my_gas_car_1.gas_tank.percentage, 60)
        self.assertEqual(test_my_gas_car_1.direction, DrivingDirection.LEFT)
        self.assertEqual(test_my_gas_car_1.position.x, -60)
        self.assertEqual(test_my_gas_car_1.set_present_coordinate_direction.current_coordinate_direction, CoordinateDirection.X_MINUS)
    
    def test_drive_foward_60_then_turn_left_120_and_add_name(self):
        # Arrange
        test_my_gas_car_1 = GasCar('Toyota', 'Corolla', 2017)
        test_my_gas_car_1.add_gas_tank(GasTank(15, 0.05))
        test_my_gas_car_1.drive(DrivingDirection.FORWARD, 60)
        test_my_gas_car_1.assigned_driver("John")
       
        # Act
        test_my_gas_car_1.drive(DrivingDirection.LEFT, 60)

        # Assert
        self.assertEqual(test_my_gas_car_1.miles_drove, 120)
        self.assertEqual(test_my_gas_car_1.gas_tank.capacity_left, 9)
        self.assertEqual(test_my_gas_car_1.gas_tank.percentage, 60)
        self.assertEqual(test_my_gas_car_1.direction, DrivingDirection.LEFT)
        self.assertEqual(test_my_gas_car_1.position.x, -60)
        self.assertEqual(test_my_gas_car_1.set_present_coordinate_direction.current_coordinate_direction, CoordinateDirection.X_MINUS)
        self.assertEqual(test_my_gas_car_1.driver.name, "John")
    
    def test_drive_foward_60_then_turn_left_120_add_name_and_seat_number(self):
        # Arrange
        test_my_gas_car_1 = GasCar('Toyota', 'Corolla', 2017)
        test_my_gas_car_1.add_gas_tank(GasTank(15, 0.05))
        test_my_gas_car_1.drive(DrivingDirection.FORWARD, 60)
        test_my_gas_car_1.assigned_driver("John")
        test_my_gas_car_1.seat_number(4)
       
        # Act
        test_my_gas_car_1.drive(DrivingDirection.LEFT, 60)

        # Assert
        self.assertEqual(test_my_gas_car_1.miles_drove, 120)
        self.assertEqual(test_my_gas_car_1.gas_tank.capacity_left, 9)
        self.assertEqual(test_my_gas_car_1.gas_tank.percentage, 60)
        self.assertEqual(test_my_gas_car_1.direction, DrivingDirection.LEFT)
        self.assertEqual(test_my_gas_car_1.position.x, -60)
        self.assertEqual(test_my_gas_car_1.set_present_coordinate_direction.current_coordinate_direction, CoordinateDirection.X_MINUS)
        self.assertEqual(test_my_gas_car_1.driver.name, "John")
        self.assertEqual(test_my_gas_car_1.seat.number, 4)
    
    def test_drive_foward_60_then_turn_left_120_add_name_seat_number_and_passenger(self):
        # Arrange
        test_my_gas_car_1 = GasCar('Toyota', 'Corolla', 2017)
        test_my_gas_car_1.add_gas_tank(GasTank(15, 0.05))
        test_my_gas_car_1.drive(DrivingDirection.FORWARD, 60)
        test_my_gas_car_1.assigned_driver("John")
        test_my_gas_car_1.seat_number(4)
        test_my_gas_car_1.add_passenger("Jamie")
       
        # Act
        test_my_gas_car_1.drive(DrivingDirection.LEFT, 60)

        # Assert
        self.assertEqual(test_my_gas_car_1.miles_drove, 120)
        self.assertEqual(test_my_gas_car_1.gas_tank.capacity_left, 9)
        self.assertEqual(test_my_gas_car_1.gas_tank.percentage, 60)
        self.assertEqual(test_my_gas_car_1.direction, DrivingDirection.LEFT)
        self.assertEqual(test_my_gas_car_1.position.x, -60)
        self.assertEqual(test_my_gas_car_1.set_present_coordinate_direction.current_coordinate_direction, CoordinateDirection.X_MINUS)
        self.assertEqual(test_my_gas_car_1.driver.name, "John")
        self.assertEqual(test_my_gas_car_1.seat.number, 4)
        self.assertEqual(test_my_gas_car_1.passenger.name, "Jamie")
    
    def test_tire_pressure(self):
        # Arrange
        test_my_gas_car_1 = GasCar('Toyota', 'Corolla', 2017)
        test_my_gas_car_1.add_gas_tank(GasTank(15, 0.05))
       
        # Act
        test_my_gas_car_1.inflation(15, "yes")

        # Assert
        #self.assertEqual(test_my_gas_car_1.inflation, 35)
    
    """ def test_drive_reverse_turn(self):
        # Arrange
        test_my_gas_car_1 = GasCar('Toyota', 'Corolla', 2017, 15, 0.05)
        test_my_gas_car_1.drive(DrivingDirection.FORWARD, 60)
        test_my_gas_car_1.drive(DrivingDirection.LEFT, 120)

        # Act
        test_my_gas_car_1.drive(DrivingDirection.BACKWARD, 120)

        # Assert
        self.assertEqual(test_my_gas_car_1.miles_drove, 300)
        self.assertEqual(test_my_gas_car_1.gas_tank.capacity_left, 0)
        self.assertEqual(test_my_gas_car_1.gas_tank.percentage, 0)
        self.assertEqual(test_my_gas_car_1.direction, DrivingDirection.BACKWARD)
    
    def test_drive_complete_circle(self):
        # Arrange
        test_my_gas_car_1 = GasCar('Toyota', 'Corolla', 2017, 15, 0.05)
        test_my_gas_car_1.drive(DrivingDirection.FORWARD, 60)
        test_my_gas_car_1.drive(DrivingDirection.LEFT, 120)
        test_my_gas_car_1.drive(DrivingDirection.BACKWARD, 120)

        # Act
        test_my_gas_car_1.fill_gas()
        test_my_gas_car_1.drive(DrivingDirection.RIGHT, 60)

        # Assert
        self.assertEqual(test_my_gas_car_1.miles_drove, 360)
        self.assertEqual(test_my_gas_car_1.gas_tank.capacity_left, 12)
        self.assertEqual(test_my_gas_car_1.gas_tank.percentage, 80)
        self.assertEqual(test_my_gas_car_1.direction, DrivingDirection.RIGHT)

        #test_my_gas_car_1.fill_gas(0.5)
        #self.assertEqual(test_my_gas_car_1.capacity, 15)
     """
    # def test_driving_with_tank_half_full(self):
    #     test_gas_tank_3 = GasCar('Hyundai', 'Kona', 2023)
    #     test_gas_tank_3.move_with_gas(5, "left", 4)
    #     test_gas_tank_3.turn_left(4)
    #     self.assertEqual(test_gas_tank_3.read_odometer(), 4)

    # def test_refuel(self):
    #     test_gas_tank_5 = GasCar('Honda', 'Civic', 2020)
    #     test_gas_tank_5.move_with_gas(10, "backward", 10)
    #     test_gas_tank_5.drive_backward(6)
    #     test_gas_tank_5.turn_left(4)
    #     self.assertEqual(test_gas_tank_5.read_odometer(), 10)

if __name__ == '__main__':
    unittest.main()