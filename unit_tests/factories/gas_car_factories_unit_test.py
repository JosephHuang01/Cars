import unittest

from factories.gas_car_factory import GasCarFactory
from factories.build_specification import BuildSpecification

class TestGasCarFactories(unittest.TestCase):
    def test_original_gas_car(self):
        # Arrange
        factory_1 = GasCarFactory()
        build_specification = BuildSpecification()
        build_specification.make = 'Toyota'
        build_specification.model = 'Corolla'
        build_specification.year = 2017
        build_specification.gas_tank_capacity = 15

        # Act
        gas_car_1 = factory_1.build_gas_car(build_specification)
        
        # Assert
        self.assertEqual(gas_car_1.make, 'Toyota')
        self.assertEqual(gas_car_1.model, 'Corolla')
        self.assertEqual(gas_car_1.year, 2017)
        self.assertEqual(gas_car_1.gas_tank.capacity, 15)
    
    def test_gas_car_with_assembly_line(self):
        # Arrange
        factory_1 = GasCarFactory()
        build_specification = BuildSpecification();
        build_specification.make = 'Toyota'
        build_specification.model = 'Corolla'
        build_specification.year = 2017
        build_specification.gas_tank_capacity = 15

        # Act
        gas_car_1 = factory_1.build_gas_car(build_specification)
        
        # Assert
        self.assertEqual(gas_car_1.make, 'Toyota')
        self.assertEqual(gas_car_1.model, 'Corolla')
        self.assertEqual(gas_car_1.year, 2017)
        self.assertEqual(gas_car_1.gas_tank.capacity, 15)
    
    def test_gas_car_with_assembly_line_and_gas_tank(self):
        # Arrange
        factory_1 = GasCarFactory()
        build_specification = BuildSpecification();
        build_specification.make = 'Toyota'
        build_specification.model = 'Corolla'
        build_specification.year = 2017
        build_specification.gas_tank_capacity = 15

        # Act
        gas_car_1 = factory_1.build_gas_car(build_specification)
        
        # Assert
        self.assertEqual(gas_car_1.make, 'Toyota')
        self.assertEqual(gas_car_1.model, 'Corolla')
        self.assertEqual(gas_car_1.year, 2017)
        self.assertEqual(gas_car_1.gas_tank.capacity, 15)
    
    def test_default_gas_car(self):
        # Arrange
        factory_1 = GasCarFactory()
        build_specification = BuildSpecification()
        build_specification.make = 'Toyota'
        build_specification.model = 'Corolla'
        build_specification.year = 2017
        build_specification.gas_tank_capacity = 15

        # Act
        gas_car_1 = factory_1.build_gas_car(build_specification)
        
        # Assert
        self.assertEqual(gas_car_1.make, 'Toyota')
        self.assertEqual(gas_car_1.model, 'Corolla')
        self.assertEqual(gas_car_1.year, 2017)
        self.assertEqual(gas_car_1.gas_tank.capacity, 15)
unittest.main()