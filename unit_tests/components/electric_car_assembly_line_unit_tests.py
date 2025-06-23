import unittest
from factories.electric_car_assembly_line import ElectricCarAssemblyLine

class TestElectricCar(unittest.TestCase):
    def test_assembled_electric_car(self):
        # Arrange
        electric_car_assembly_line = ElectricCarAssemblyLine()

        # Act
        test_my_electric_car_1 = electric_car_assembly_line.assemble_car_model('Tesla', 'S6', 2024)

        # Assert
        self.assertEqual(test_my_electric_car_1.make, 'Tesla')
        self.assertEqual(test_my_electric_car_1.model, 'S6')
        self.assertEqual(test_my_electric_car_1.year, 2024)

        #test_my_electric_car_1.include_battery(70, 0.2)
        #test_my_electric_car_1.build_model()

unittest.main()