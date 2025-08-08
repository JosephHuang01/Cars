from components.map import Map
from components.shape import ShapeSpecification
from components.position import Position
import unittest

class TestMap(unittest.TestCase):
    def setUp(self):
        shape_spec = ShapeSpecification()
        shape_spec.position = Position(0, 0)
        shape_spec.width = 1536
        shape_spec.length = 800
        self.map = Map(None, None, shape_spec)

        self.road_specs = [
            (75, 41, 18, 135),
            (201, 41, 457, 18),
            (235, 498, 18, 394),
            (611, 516, 169, 18),
            (629, 656, 18, 626),
            (1271, 81, 559, 18),
            (1289, 81, 18, 147),
            (846, 156, 18, 425),
            (219, 156, 18, 577),
        ]

        for x, y, length, width in self.road_specs:
            road_spec = ShapeSpecification()
            road_spec.position = Position(x, y)
            road_spec.length = length
            road_spec.width = width
            road = Map(None, None, road_spec)
            self.map.add_road(road)

    def test_on_road(self):
        # Act
        position_on_road_one = self.map.is_position_on_road(Position(100, 49))
        position_on_road_two = self.map.is_position_on_road(Position(215, 480))
        position_on_road_three = self.map.is_position_on_road(Position(625, 510))
        position_on_road_four = self.map.is_position_on_road(Position(625, 625))
        position_on_road_five = self.map.is_position_on_road(Position(1250, 670))
        position_on_road_six = self.map.is_position_on_road(Position(1285, 600))
        position_on_road_seven = self.map.is_position_on_road(Position(1335, 95))
        position_on_road_eight = self.map.is_position_on_road(Position(1270, 170))
        position_on_road_nine = self.map.is_position_on_road(Position(595, 170))
        
        # Assert
        self.assertEqual(position_on_road_one, True)
        self.assertEqual(position_on_road_two, True)
        self.assertEqual(position_on_road_three, True)
        self.assertEqual(position_on_road_four, True)
        self.assertEqual(position_on_road_five, True)
        self.assertEqual(position_on_road_six, True)
        self.assertEqual(position_on_road_seven, True)
        self.assertEqual(position_on_road_eight, True)
        self.assertEqual(position_on_road_nine, True)
        
    def test_not_on_road(self):
        # Act
        position_near_road_one_and_two = self.map.is_position_on_road(Position(70, 45))
        position_near_road_three_and_four = self.map.is_position_on_road(Position(423, 520))
        position_near_road_five = self.map.is_position_on_road(Position(942, 697))
        position_near_road_six = self.map.is_position_on_road(Position(1313, 320))
        position_near_road_nine = self.map.is_position_on_road(Position(605, 150))
        center = self.map.is_position_on_road(Position(768, 400))

        # Assert
        self.assertEqual(position_near_road_one_and_two, False)
        self.assertEqual(position_near_road_three_and_four, False)
        self.assertEqual(position_near_road_five, False)
        self.assertEqual(position_near_road_six, False)
        self.assertEqual(position_near_road_nine, False)
        self.assertEqual(center, False)
    
    def test_on_cities(self):
        # Act
        seattle = self.map.is_position_on_road(Position(60, 70))
        los_angeles = self.map.is_position_on_road(Position(200, 500))
        dallas = self.map.is_position_on_road(Position(640, 730))
        atlanta = self.map.is_position_on_road(Position(1300, 665))
        new_york = self.map.is_position_on_road(Position(1480, 100))
        chicago = self.map.is_position_on_road(Position(845, 170))
        
        # Assert
        self.assertEqual(seattle, False)
        self.assertEqual(los_angeles, False)
        self.assertEqual(dallas, False)
        self.assertEqual(atlanta, False)
        self.assertEqual(new_york, False)
        self.assertEqual(chicago, False)

unittest.main()