import unittest

from factories.electric_car_factory import ElectricCarFactory
from factories.build_specification import BuildSpecification

class TestElectricCarFactories(unittest.TestCase):
    def test_original_electric_car(self):
        # Arrange
        factory_1 = ElectricCarFactory()
        build_specification = BuildSpecification()
        build_specification.make = 'Tesla'
        build_specification.model = 'S6'
        build_specification.year = 2024
        build_specification.battery_capacity = 70

        # Act
        electric_car_1 = factory_1.build_electric_car(build_specification)

        # Assert
        self.assertEqual(electric_car_1.make, 'Tesla')
        self.assertEqual(electric_car_1.model, 'S6')
        self.assertEqual(electric_car_1.year, 2024)
        self.assertEqual(electric_car_1.battery.capacity, 70)
    
    def test_electric_car_with_battery(self):
        # Arrange
        factory_1 = ElectricCarFactory()
        build_specification = BuildSpecification()
        build_specification.make = 'Tesla'
        build_specification.model = 'S6'
        build_specification.year = 2024
        build_specification.battery_capacity = 70

        # Act
        electric_car_1 = factory_1.build_electric_car(build_specification)

        # Assert
        self.assertEqual(electric_car_1.make, 'Tesla')
        self.assertEqual(electric_car_1.model, 'S6')
        self.assertEqual(electric_car_1.year, 2024)
        self.assertEqual(electric_car_1.battery.capacity, 70)
    
    def test_default_electric_car(self):
        # Arrange
        factory_1 = ElectricCarFactory()
        build_specification = BuildSpecification()
        build_specification.make = 'Tesla'
        build_specification.model = 'S6'
        build_specification.year = 2024
        build_specification.battery_capacity = 70

        # Act
        electric_car_1 = factory_1.build_electric_car(build_specification)

        # Assert
        self.assertEqual(electric_car_1.make, 'Tesla')
        self.assertEqual(electric_car_1.model, 'S6')
        self.assertEqual(electric_car_1.year, 2024)
        self.assertEqual(electric_car_1.battery.capacity, 70)

unittest.main()