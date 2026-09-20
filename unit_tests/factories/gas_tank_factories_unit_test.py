import unittest

from factories.gas_tank_factory import GasTankFactory

class TestGasTankFactories(unittest.TestCase):
    def test_original_gas_tank(self):
        # Arrange
        factory_1 = GasTankFactory()
        test_gas_tank_capacity = 15

        # Act
        gas_tank_1 = factory_1.build_gas_tank(test_gas_tank_capacity)

        # Assert
        self.assertEqual(gas_tank_1.capacity, test_gas_tank_capacity)

unittest.main()