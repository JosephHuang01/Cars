import unittest
from components.position import Position

class TestPosition(unittest.TestCase):
    def setUp(self):
        # Arrange
        self.current_position = Position(1125, 1800)

        

    def test_distance_1(self):
        # Arrange
        original_position = Position(0, 0)

        # Act
        new_position = Position(3, 4)

        # Assert
        self.assertEqual(original_position.get_distance(new_position), 5)

    def test_distance_2(self):
        # Arrange
        original_position = Position(0, 0)

        # Act
        new_position = Position(3, 4)

        # Assert
        self.assertEqual(original_position.get_distance(new_position), 5)
    
    def test_directions_1(self):
        # Act
        self.directions = self.current_position.get_positions_in_four_directions(1000)

        position1 = Position(2125, 1800)
        # Assert
        self.assertEqual(True, position1.is_same_position(self.directions[0]))
        self.assertEqual(self.directions[1].x, 125)
        self.assertEqual(self.directions[1].y, 1800)
        self.assertEqual(self.directions[2].x, 1125)
        self.assertEqual(self.directions[2].y, 2800)
        self.assertEqual(self.directions[2].x, 1125)
        self.assertEqual(self.directions[2].y, 2800)

if __name__ == "__main__":
    unittest.main()