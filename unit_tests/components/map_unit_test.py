from components.map import Map
from components.shape import ShapeSpecification
from components.position import Position
import unittest

class TestMap(unittest.TestCase):
    def test_one(self):
        # Arrange
        shape_spec = ShapeSpecification()
        shape_spec.position = Position(0, 0)
        shape_spec.width = 600
        shape_spec.length = 450
        map = Map(None, None, shape_spec)

        road_spec = ShapeSpecification()
        road_spec.position = Position(150, 160)
        road_spec.length = 20
        road_spec.width = 410
        road = Map(None, None, road_spec)

        map.add_road(road)
        
        # Act
        position_on_road = map.is_position_on_road(Position(155, 170))

        # Assert
        self.assertEqual(position_on_road, True)

unittest.main()