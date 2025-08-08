from components.map import Map
from components.shape import ShapeSpecification
from components.position import Position
import unittest

class TestCities(unittest.TestCase):
    def setUp(self):
        shape_spec = ShapeSpecification()
        shape_spec.position = Position(0, 0)
        shape_spec.width = 1536
        shape_spec.length = 800
        self.map = Map(None, None, shape_spec)

        self.city_specs = [
            (25, 25, 50, 50),
            (185, 482, 50, 50),
            (595, 685, 50, 50),
            (1255, 640, 50, 50),
            (1436, 65, 50, 50),
            (796, 140, 50, 50)
        ]

        for x, y, length, width in self.city_specs:
            city_spec = ShapeSpecification()
            city_spec.position = Position(x, y)
            city_spec.length = length
            city_spec.width = width
            city = Map(None, None, city_spec)
            self.map.add_city(city)
            
        return super().setUp()

    def test_city(self):
        # Act
        position_on_seattle = self.map.is_position_on_city(Position(60, 70))
        position_on_los_angeles = self.map.is_position_on_city(Position(200, 500))
        position_on_dallas = self.map.is_position_on_city(Position(640, 730))
        position_on_atlanta = self.map.is_position_on_city(Position(1300, 665))
        position_on_new_york = self.map.is_position_on_city(Position(1480, 100))
        position_on_chicago = self.map.is_position_on_city(Position(845, 170))

        # Assert
        self.assertEqual(position_on_seattle, True)
        self.assertEqual(position_on_los_angeles, True)
        self.assertEqual(position_on_dallas, True)
        self.assertEqual(position_on_atlanta, True)
        self.assertEqual(position_on_new_york, True)
        self.assertEqual(position_on_chicago, True)
        
unittest.main()