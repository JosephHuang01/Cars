import unittest
from components.shape import Shape, ShapeSpecification
from components.position import Position

class TestShape(unittest.TestCase):
    def test_position_inside_the_shape_true(self):
        # Arrange
        shape_spec = ShapeSpecification()
        shape_spec.position = Position(0, 0)
        shape_spec.width = 1600
        shape_spec.length = 800
        shape = Shape(None, None, shape_spec)

        # Act
        car_in_road = shape.is_inside_the_shape(Position(400, 400))

        # Assert
        self.assertEqual(car_in_road, True)
    
    def test_position_top_outside_the_shape_false(self):
        # Arrange
        shape_spec = ShapeSpecification()
        shape_spec.position = Position(400, 400)
        shape_spec.width = 1600
        shape_spec.length = 800
        shape = Shape(None, None, shape_spec)

        # Act
        car_in_road = shape.is_inside_the_shape(Position(200, 500))

        # Assert
        self.assertEqual(car_in_road, False)
    
    def test_right(self):
        # Arrange
        shape_spec = ShapeSpecification()
        shape_spec.position = Position(0, 0)
        shape_spec.width = 1600
        shape_spec.length = 800
        shape = Shape(None, None, shape_spec)

        # Act
        car_in_road = shape.is_inside_the_shape(Position(900, 400))

        # Assert
        self.assertEqual(car_in_road, True)
    
    def test_down(self):
        # Arrange
        shape_spec = ShapeSpecification()
        shape_spec.position = Position(0, 0)
        shape_spec.width = 1600
        shape_spec.length = 800
        shape = Shape(None, None, shape_spec)

        # Act
        car_in_road = shape.is_inside_the_shape(Position(900, 550))

        # Assert
        self.assertEqual(car_in_road, True)
    
    def test_left(self):
        # Arrange
        shape_spec = ShapeSpecification()
        shape_spec.position = Position(0, 0)
        shape_spec.width = 1600
        shape_spec.length = 800
        shape = Shape(None, None, shape_spec)

        # Act
        car_in_road = shape.is_inside_the_shape(Position(300, 550))

        # Assert
        self.assertEqual(car_in_road, True)
    
    def test_up(self):
        # Arrange
        shape_spec = ShapeSpecification()
        shape_spec.position = Position(0, 0)
        shape_spec.width = 1600
        shape_spec.length = 800
        shape = Shape(None, None, shape_spec)

        # Act
        car_in_road = shape.is_inside_the_shape(Position(100, 550))

        # Assert
        self.assertEqual(car_in_road, True)
    
    def test_pos(self):
        # Arrange
        shape_spec = ShapeSpecification()
        shape_spec.position = Position(500, 500)
        shape_spec.width = 300
        shape_spec.length = 500
        shape = Shape(None, None, shape_spec)

        # Act
        test_pos_1 = shape.is_inside_the_shape(Position(300, 700))
        test_pos_2 = shape.is_inside_the_shape(Position(300, 600))
        test_pos_3 = shape.is_inside_the_shape(Position(900, 700))
        test_pos_4 = shape.is_inside_the_shape(Position(600, 1200))
        test_pos_5 = shape.is_inside_the_shape(Position(600, 700))

        # Assert
        self.assertEqual(test_pos_1, False)
        self.assertEqual(test_pos_2, False)
        self.assertEqual(test_pos_3, False)
        self.assertEqual(test_pos_4, False)
        self.assertEqual(test_pos_5, True)

unittest.main()