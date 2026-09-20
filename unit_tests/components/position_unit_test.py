import unittest
from components.position import Position

class TestPosition(unittest.TestCase):
    def test_distance_1(self):
        # Arrange
        original_position = Position(0, 0)

        # Act
        new_position = Position(3, 4)

        # Assert
        self.assertEqual(original_position.get_distance(new_position), 5)
    
    def test_distance_northeast(self):
        # Arrange
        original_position = Position(125, 85)
        destination = Position(700, 150)
        expected_shortest_position = Position(135, 85) or Position(125, 95)

        # Act
        proposed_destinations = original_position.get_positions_in_four_directions(10)
        calculated_shortest_position = destination.find_shortest_distance_to_position(proposed_destinations)

        # Assert
        self.assertEqual(True, expected_shortest_position.is_same_position(calculated_shortest_position))
    
    def test_distance_southeast(self):
        # Arrange
        original_position = Position(125, 85)
        destination = Position(700, 50)
        expected_shortest_position = Position(135, 85) or Position(125, 75)

        # Act
        proposed_destinations = original_position.get_positions_in_four_directions(10)
        calculated_shortest_position = destination.find_shortest_distance_to_position(proposed_destinations)

        # Assert
        self.assertEqual(True, expected_shortest_position.is_same_position(calculated_shortest_position))
    
    def test_distance_southwest(self):
        # Arrange
        original_position = Position(125, 85)
        destination = Position(50, 50)
        expected_shortest_position = Position(115, 85) or Position(125, 75)

        # Act
        proposed_destinations = original_position.get_positions_in_four_directions(10)
        calculated_shortest_position = destination.find_shortest_distance_to_position(proposed_destinations)

        # Assert
        self.assertEqual(True, expected_shortest_position.is_same_position(calculated_shortest_position))
    
    def test_distance_northwest(self):
        # Arrange
        original_position = Position(125, 85)
        destination = Position(50, 150)
        expected_shortest_position = Position(115, 85) or Position(125, 95)

        # Act
        proposed_destinations = original_position.get_positions_in_four_directions(10)
        calculated_shortest_position = destination.find_shortest_distance_to_position(proposed_destinations)

        # Assert
        self.assertEqual(True, expected_shortest_position.is_same_position(calculated_shortest_position))

    def test_distance_horizontal_right(self):
        # Arrange
        original_position = Position(125, 85)
        proposed_destinations = original_position.get_positions_in_four_directions(10)
        destination = Position(700, 85)
        expected_shortest_position = Position(135, 85)

        # Act
        calculated_shortest_position = destination.find_shortest_distance_to_position(proposed_destinations)

        # Assert
        self.assertEqual(True, expected_shortest_position.is_same_position(calculated_shortest_position))
    
    def test_distance_horizontal_left(self):
        # Arrange
        original_position = Position(125, 85)
        proposed_destinations = original_position.get_positions_in_four_directions(10)
        destination = Position(50, 85)
        expected_shortest_position = Position(115, 85)

        # Act        
        calculated_shortest_position = destination.find_shortest_distance_to_position(proposed_destinations)

        # Assert
        self.assertEqual(True, expected_shortest_position.is_same_position(calculated_shortest_position))
    
    def test_distance_vertical_up(self):
        # Arrange
        original_position = Position(125, 85)
        destination = Position(125, 150)
        expected_shortest_position = Position(125, 95)

        # Act
        proposed_destinations = original_position.get_positions_in_four_directions(10)
        calculated_shortest_position = destination.find_shortest_distance_to_position(proposed_destinations)

        # Assert
        self.assertEqual(True, expected_shortest_position.is_same_position(calculated_shortest_position))
    
    def test_distance_horizontal_down(self):
        # Arrange
        original_position = Position(125, 85)
        destination = Position(125, 50)
        expected_shortest_position = Position(125, 75)

        # Act
        proposed_destinations = original_position.get_positions_in_four_directions(10)
        calculated_shortest_position = destination.find_shortest_distance_to_position(proposed_destinations)

        # Assert
        self.assertEqual(True, expected_shortest_position.is_same_position(calculated_shortest_position))
    
    def test_directions_1(self):
        # Arrange
        current_position = Position(1125, 1800)

        # Act
        directions = current_position.get_positions_in_four_directions(1000)
        position1 = Position(2125, 1800)

        # Assert
        self.assertEqual(True, position1.is_same_position(directions[0]))
        self.assertEqual(directions[1].x, 125)
        self.assertEqual(directions[1].y, 1800)
        self.assertEqual(directions[2].x, 1125)
        self.assertEqual(directions[2].y, 2800)
        self.assertEqual(directions[3].x, 1125)
        self.assertEqual(directions[3].y, 800)
    
    def test_directions_2(self):
        # Arrange
        current_position = Position(600, 700)

        # Act
        directions = current_position.get_positions_in_four_directions(300)
        position1 = Position(900, 700)
        position2 = Position(300, 700)
        position3 = Position(600, 1000)
        position4 = Position(600, 400)

        # Assert
        self.assertEqual(True, position1.is_same_position(directions[0]))
        self.assertEqual(True, position2.is_same_position(directions[1]))
        self.assertEqual(True, position3.is_same_position(directions[2]))
        self.assertEqual(True, position4.is_same_position(directions[3]))

if __name__ == "__main__":
    unittest.main()