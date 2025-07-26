import unittest
from services.driving import SelfDrivingCar
from components.position import Position
from components.car import Car

class TestDriving(unittest.TestCase):
    def test_vertical_down_10(self):
        # Arrange
        car = SelfDrivingCar(Car)
        starting_position = Position(100, 100)
        ending_position = Position(100, 400)
        expected_path = Position(100, 110)
        car.set_start_position(starting_position)
        car.add_destination(ending_position)

        # Act
        car.drive()
        new_position = car.current_position

        # Assert
        self.assertEqual(True, new_position.is_same_position(expected_path))

    def test_vertical_down_20(self):
        # Arrange
        car = SelfDrivingCar(Car)
        starting_position = Position(100, 100)
        ending_position = Position(100, 400)
        expected_path = Position(100, 120)
        car.set_start_position(starting_position)
        car.add_destination(ending_position)

        # Act
        car.drive()
        car.drive() # drive 2nd time
        new_position = car.current_position

        # Assert
        self.assertEqual(True, new_position.is_same_position(expected_path))

    def test_vertical_down_10_times(self):
        # Arrange
        car = SelfDrivingCar(Car)
        starting_position = Position(100, 100)
        ending_position = Position(100, 400)
        expected_path = Position(100, 200)
        car.set_start_position(starting_position)
        car.add_destination(ending_position)

        # Act
        i = 1
        while i <= 10:            
            car.drive()
            i += 1
                
        new_position = car.current_position

        # Assert
        self.assertEqual(True, new_position.is_same_position(expected_path))

    def test_to_destinatin(self):
        # Arrange
        car = SelfDrivingCar(Car)
        starting_position = Position(100, 100)
        ending_position = Position(200, 400)
        expected_path = ending_position
        car.set_start_position(starting_position)
        car.add_destination(ending_position)

        # Act
        i = 1
        while i <= 100:            
            car.drive()
            print (i, "reach position:", car.current_position)
            i += 1
                
        new_position = car.current_position
        # Assert
        self.assertEqual(True, new_position.is_same_position(expected_path))

unittest.main()