import unittest
from datetime import datetime, timedelta
from database import car_explorer
from components.car import Car

class TestCarExplorer(unittest.TestCase):
    def test_car_one(self):
        # Arrange
        test_car_explorer = car_explorer.CarExplorer()

        # Act
        test_car = test_car_explorer.get_one_car()

        # Assert
        self.assertIsInstance(test_car, Car)
    
    def test_last_position(self):
        # Arrange
        test_car_explorer = car_explorer.CarExplorer()

        # Act
        test_position = test_car_explorer.get_last_trip_position(1)

        # Assert
        #self.assertEqual(test_position.x, 6.5)
        #self.assertEqual(test_position.y, 2.5)
        self.assertEqual(test_position.x, 2.5)
        self.assertEqual(test_position.y, 2.5)
    
    def test_last_position_for_car_2(self):
        # Arrange
        test_car_explorer = car_explorer.CarExplorer()

        # Act
        test_position = test_car_explorer.get_last_trip_position(2)

        # Assert
        self.assertEqual(test_position.x, 1.5)
        self.assertEqual(test_position.y, 2.5)
    
    def test_last_position_for_car_3(self):
        # Arrange
        test_car_explorer = car_explorer.CarExplorer()

        # Act
        test_position = test_car_explorer.get_last_trip_position(3)

        # Assert
        self.assertEqual(test_position.x, 0.5)
        self.assertEqual(test_position.y, 6.5)
    
    def test_save_car_trip(self):
        # Arrange
        test_car_explorer = car_explorer.CarExplorer()

        # Act
        start_time = datetime(2025, 7, 1, 4, 34, 7)
        end_time = start_time + timedelta(minutes = 3)
        test_save_trip = test_car_explorer.save_trip(1, 6.5, 0.5, 2.5, 2.5, start_time, end_time)

        # Assert
        self.assertEqual(test_save_trip, datetime(2025, 7, 1, 4, 37, 7))
        
unittest.main()