import unittest
from factories.gas_car_assembly_line import GasCarAssemblyLine
from components.car import *

class TestAssembledCar(unittest.TestCase):
    def test_assembled_gas_car(self):
        # Arrange
        gas_car_assembly_line = GasCarAssemblyLine()

        # Act
        a_car = gas_car_assembly_line.assemble_car_model('Toyota', 'Corolla', 2017)

        # Assert
        self.assertEqual(a_car.make, 'Toyota')

unittest.main()