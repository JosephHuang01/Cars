import unittest

from components.car import DrivingDirection, Car, CoordinateDirection

class TestCarCase(unittest.TestCase):
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

    def test_drive_forward_60(self):
        # Arrange
        test_my_gas_car_1 = Car('Toyota', 'Corolla', 2017)

        # Act
        test_my_gas_car_1.drive(DrivingDirection.FORWARD, 60)

        # Assert
        self.assertEqual(test_my_gas_car_1.direction, DrivingDirection.FORWARD)
        self.assertEqual(test_my_gas_car_1.position.y, 60)
        self.assertEqual(test_my_gas_car_1.set_present_coordinate_direction.current_coordinate_direction, CoordinateDirection.Y_PLUS)

    def test_drive_forward_60_then_turn_right_70(self):
        # Arrange
        test_my_gas_car_1 = Car('Toyota', 'Corolla', 2017)
        test_my_gas_car_1.drive(DrivingDirection.FORWARD, 60)

        # Act
        test_my_gas_car_1.drive(DrivingDirection.RIGHT, 70)

        # Assert
        self.assertEqual(test_my_gas_car_1.direction, DrivingDirection.RIGHT)
        self.assertEqual(test_my_gas_car_1.position.x, 70)
        self.assertEqual(test_my_gas_car_1.set_present_coordinate_direction.current_coordinate_direction, CoordinateDirection.X_PLUS)

    def test_drive_forward_60_then_turn_right_70_and_back_30(self):
        # Arrange
        test_my_gas_car_1 = Car('Toyota', 'Corolla', 2017)
        test_my_gas_car_1.drive(DrivingDirection.FORWARD, 60)
        test_my_gas_car_1.drive(DrivingDirection.RIGHT, 70)

        # Act
        test_my_gas_car_1.drive(DrivingDirection.BACKWARD, 30)

        # Assert
        self.assertEqual(test_my_gas_car_1.direction, DrivingDirection.BACKWARD)
        self.assertEqual(test_my_gas_car_1.position.y, 30)
        self.assertEqual(test_my_gas_car_1.set_present_coordinate_direction.current_coordinate_direction, CoordinateDirection.Y_MINUS)

    def test_drive_forward_60_then_turn_right_70_and_back_30_and_turn_left_45(self):
        # Arrange
        test_my_gas_car_1 = Car('Toyota', 'Corolla', 2017)
        test_my_gas_car_1.drive(DrivingDirection.FORWARD, 60)
        test_my_gas_car_1.drive(DrivingDirection.RIGHT, 70)
        test_my_gas_car_1.drive(DrivingDirection.BACKWARD, 30)

        # Act
        test_my_gas_car_1.drive(DrivingDirection.LEFT, 45)

        # Assert
        self.assertEqual(test_my_gas_car_1.direction, DrivingDirection.LEFT)
        self.assertEqual(test_my_gas_car_1.position.x, 25)
        self.assertEqual(test_my_gas_car_1.set_present_coordinate_direction.current_coordinate_direction, CoordinateDirection.X_MINUS)

    def test_drive_back_60(self):
        # Arrange
        test_my_gas_car_1 = Car('Toyota', 'Corolla', 2017)

        # Act
        test_my_gas_car_1.drive(DrivingDirection.BACKWARD, 60)

        # Assert
        self.assertEqual(test_my_gas_car_1.direction, DrivingDirection.BACKWARD)
        self.assertEqual(test_my_gas_car_1.position.y, -60)
        self.assertEqual(test_my_gas_car_1.set_present_coordinate_direction.current_coordinate_direction, CoordinateDirection.Y_MINUS)

    def test_drive_back_60_then_turn_left_70(self):
        # Arrange
        test_my_gas_car_1 = Car('Toyota', 'Corolla', 2017)
        test_my_gas_car_1.drive(DrivingDirection.BACKWARD, 60)

        # Act
        test_my_gas_car_1.drive(DrivingDirection.LEFT, 70)

        # Assert
        self.assertEqual(test_my_gas_car_1.direction, DrivingDirection.LEFT)
        self.assertEqual(test_my_gas_car_1.position.x, -70)
        self.assertEqual(test_my_gas_car_1.set_present_coordinate_direction.current_coordinate_direction, CoordinateDirection.X_MINUS)

    def test_drive_back_60_and_then_forward_30(self):
        # Arrange
        test_my_gas_car_1 = Car('Toyota', 'Corolla', 2017)
        test_my_gas_car_1.drive(DrivingDirection.BACKWARD, 60)

        # Act
        test_my_gas_car_1.drive(DrivingDirection.FORWARD, 30)

        # Assert
        self.assertEqual(test_my_gas_car_1.direction, DrivingDirection.FORWARD)
        self.assertEqual(test_my_gas_car_1.position.y, -30)
        self.assertEqual(test_my_gas_car_1.set_present_coordinate_direction.current_coordinate_direction, CoordinateDirection.Y_MINUS)
    
    def test_drive_back_60_and_then_right_45(self):
        # Arrange
        test_my_gas_car_1 = Car('Toyota', 'Corolla', 2017)
        test_my_gas_car_1.drive(DrivingDirection.BACKWARD, 60)

        # Act
        test_my_gas_car_1.drive(DrivingDirection.RIGHT, 45)

        # Assert
        self.assertEqual(test_my_gas_car_1.direction, DrivingDirection.RIGHT)
        self.assertEqual(test_my_gas_car_1.position.x, 45)
        self.assertEqual(test_my_gas_car_1.set_present_coordinate_direction.current_coordinate_direction, CoordinateDirection.X_PLUS)

    def test_drive_right_60(self):
        # Arrange
        test_my_gas_car_1 = Car('Toyota', 'Corolla', 2017)

        # Act
        test_my_gas_car_1.drive(DrivingDirection.RIGHT, 60)

        # Assert
        self.assertEqual(test_my_gas_car_1.direction, DrivingDirection.RIGHT)
        self.assertEqual(test_my_gas_car_1.position.x, 60)
        self.assertEqual(test_my_gas_car_1.set_present_coordinate_direction.current_coordinate_direction, CoordinateDirection.X_PLUS)
    
    def test_drive_right_60_and_then_drive_forward_70(self):
        # Arrange
        test_my_gas_car_1 = Car('Toyota', 'Corolla', 2017)
        test_my_gas_car_1.drive(DrivingDirection.RIGHT, 60)

        # Act
        test_my_gas_car_1.drive(DrivingDirection.FORWARD, 70)

        # Assert
        self.assertEqual(test_my_gas_car_1.direction, DrivingDirection.FORWARD)
        self.assertEqual(test_my_gas_car_1.position.y, 70)
        self.assertEqual(test_my_gas_car_1.set_present_coordinate_direction.current_coordinate_direction, CoordinateDirection.X_PLUS)
    
    def test_drive_right_60_and_then_turn_left_30(self):
        # Arrange
        test_my_gas_car_1 = Car('Toyota', 'Corolla', 2017)
        test_my_gas_car_1.drive(DrivingDirection.RIGHT, 60)

        # Act
        test_my_gas_car_1.drive(DrivingDirection.LEFT, 30)

        # Assert
        self.assertEqual(test_my_gas_car_1.direction, DrivingDirection.LEFT)
        self.assertEqual(test_my_gas_car_1.position.x, 30)
        self.assertEqual(test_my_gas_car_1.set_present_coordinate_direction.current_coordinate_direction, CoordinateDirection.X_MINUS)
    
    def test_drive_right_60_and_then_drive_backward_45(self):
        # Arrange
        test_my_gas_car_1 = Car('Toyota', 'Corolla', 2017)
        test_my_gas_car_1.drive(DrivingDirection.RIGHT, 60)

        # Act
        test_my_gas_car_1.drive(DrivingDirection.BACKWARD, 45)

        # Assert
        self.assertEqual(test_my_gas_car_1.direction, DrivingDirection.BACKWARD)
        self.assertEqual(test_my_gas_car_1.position.y, -45)
        self.assertEqual(test_my_gas_car_1.set_present_coordinate_direction.current_coordinate_direction, CoordinateDirection.Y_MINUS)

    def test_drive_left_60(self):
        # Arrange
        test_my_gas_car_1 = Car('Toyota', 'Corolla', 2017)

        # Act
        test_my_gas_car_1.drive(DrivingDirection.LEFT, 60)

        # Assert
        self.assertEqual(test_my_gas_car_1.direction, DrivingDirection.LEFT)
        self.assertEqual(test_my_gas_car_1.position.x, -60)
        self.assertEqual(test_my_gas_car_1.set_present_coordinate_direction.current_coordinate_direction, CoordinateDirection.X_MINUS)
    
    def test_drive_left_60_and_then_drive_forward_70(self):
        # Arrange
        test_my_gas_car_1 = Car('Toyota', 'Corolla', 2017)
        test_my_gas_car_1.drive(DrivingDirection.LEFT, 60)

        # Act
        test_my_gas_car_1.drive(DrivingDirection.FORWARD, 70)

        # Assert
        self.assertEqual(test_my_gas_car_1.direction, DrivingDirection.FORWARD)
        self.assertEqual(test_my_gas_car_1.position.y, 70)
        self.assertEqual(test_my_gas_car_1.set_present_coordinate_direction.current_coordinate_direction, CoordinateDirection.X_MINUS)
    
    def test_drive_left_60_and_then_turn_right_30(self):
        # Arrange
        test_my_gas_car_1 = Car('Toyota', 'Corolla', 2017)
        test_my_gas_car_1.drive(DrivingDirection.LEFT, 60)

        # Act
        test_my_gas_car_1.drive(DrivingDirection.RIGHT, 30)

        # Assert
        self.assertEqual(test_my_gas_car_1.direction, DrivingDirection.RIGHT)
        self.assertEqual(test_my_gas_car_1.position.x, -30)
        self.assertEqual(test_my_gas_car_1.set_present_coordinate_direction.current_coordinate_direction, CoordinateDirection.X_PLUS)
    
    def test_drive_left_60_and_then_drive_backward_45(self):
        # Arrange
        test_my_gas_car_1 = Car('Toyota', 'Corolla', 2017)
        test_my_gas_car_1.drive(DrivingDirection.LEFT, 60)

        # Act
        test_my_gas_car_1.drive(DrivingDirection.BACKWARD, 45)

        # Assert
        self.assertEqual(test_my_gas_car_1.direction, DrivingDirection.BACKWARD)
        self.assertEqual(test_my_gas_car_1.position.y, -45)
        self.assertEqual(test_my_gas_car_1.set_present_coordinate_direction.current_coordinate_direction, CoordinateDirection.Y_MINUS)

unittest.main()