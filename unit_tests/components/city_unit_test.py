import unittest
from components.city import City

class TestCity(unittest.TestCase):
    def test_atlanta(self):
        # Arrange
        atlanta = City("Atlanta", 7, 7)
        new_york = City("New York", 7, 1)
        los_angeles = City("Los Angeles", 1, 2)

        # Act
        number = City.cities
        
        # Assert
        self.assertEqual(len(number), 3)
        self.assertEqual(number[0].name, "Atlanta")
        self.assertEqual(number[0].position.x, 7)
        self.assertEqual(number[0].position.y, 7)
        self.assertEqual(number[1].name, "New York")
        self.assertEqual(number[1].position.x, 7)
        self.assertEqual(number[1].position.y, 1)
        self.assertEqual(number[2].name, "Los Angeles")
        self.assertEqual(number[2].position.x, 1)
        self.assertEqual(number[2].position.y, 2)

unittest.main()