import unittest

from factories.battery_factory import BatteryFactory

class TestBatteryFactories(unittest.TestCase):
    def test_original_factory(self):
        # Arrange
        test_battery_capacity = 70
        factory_1 = BatteryFactory()

        # Act
        battery_1 = factory_1.build_battery(test_battery_capacity)

        # Assert
        self.assertEqual(battery_1.capacity, test_battery_capacity)

unittest.main()