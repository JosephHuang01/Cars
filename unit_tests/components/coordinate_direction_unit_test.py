import unittest
from components.driving_direction import DrivingDirection
from components.car import Car, CoordinateDirection

class TestCoordinateDirection(unittest.TestCase):
    def test_coordinate_direction_after_drive_foward_60(self):
        # Arrange
        test_my_car_1 = Car('Toyota', 'Corolla', 2017)        
       
        # Act
        test_my_car_1.drive(DrivingDirection.FORWARD, 60)

        # Assert       
        self.assertEqual(test_my_car_1.direction, DrivingDirection.FORWARD)     
        self.assertEqual(test_my_car_1.set_present_coordinate_direction.current_coordinate_direction, CoordinateDirection.Y_PLUS)

    def test_coordinate_direction_after_turn_left_60_and_turn_left_60(self):
        # Arrange
        test_my_gas_car_1 = Car('Toyota', 'Corolla', 2017)     
        test_my_gas_car_1.drive(DrivingDirection.LEFT, 60)   
       
        # Act
        test_my_gas_car_1.drive(DrivingDirection.LEFT, 60)

        # Assert       
        self.assertEqual(test_my_gas_car_1.direction, DrivingDirection.LEFT)     
        self.assertEqual(test_my_gas_car_1.set_present_coordinate_direction.current_coordinate_direction, CoordinateDirection.X_MINUS)    

    def test_coordinate_direction_after_drive_foward_60_then_turn_left_120(self):
        # Arrange
        test_my_gas_car_1 = Car('Toyota', 'Corolla', 2017)
        test_my_gas_car_1.drive(DrivingDirection.FORWARD, 60)
       
        # Act
        test_my_gas_car_1.drive(DrivingDirection.LEFT, 120)

        # Assert
        self.assertEqual(test_my_gas_car_1.direction, DrivingDirection.LEFT)
        self.assertEqual(test_my_gas_car_1.set_present_coordinate_direction.current_coordinate_direction, CoordinateDirection.X_MINUS)

    def test_coordinate_direction_after_drive_foward_60_then_turn_right_120(self):
        # Arrange
        test_my_gas_car_1 = Car('Toyota', 'Corolla', 2017)
        test_my_gas_car_1.drive(DrivingDirection.FORWARD, 60)
       
        # Act
        test_my_gas_car_1.drive(DrivingDirection.RIGHT, 120)

        # Assert       
        self.assertEqual(test_my_gas_car_1.direction, DrivingDirection.RIGHT)
        self.assertEqual(test_my_gas_car_1.set_present_coordinate_direction.current_coordinate_direction, CoordinateDirection.X_PLUS)    

    def test_drive_foward_60_then_turn_left_120(self):
        # Arrange
        test_my_gas_car_1 = Car('Toyota', 'Corolla', 2017)
        test_my_gas_car_1.drive(DrivingDirection.FORWARD, 60)
       
        # Act
        test_my_gas_car_1.drive(DrivingDirection.LEFT, 120)

        # Assert
        self.assertEqual(test_my_gas_car_1.direction, DrivingDirection.LEFT)
        self.assertEqual(test_my_gas_car_1.position.x, -120)
        self.assertEqual(test_my_gas_car_1.set_present_coordinate_direction.current_coordinate_direction, CoordinateDirection.X_MINUS)

unittest.main()