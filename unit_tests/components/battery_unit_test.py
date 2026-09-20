import unittest

# All below works!!!
# python -m unit_tests.components.battery_unit_test


from components.battery import Battery
#car_1 = Battery.traveled_distance(25)


class TestBattery(unittest.TestCase):

    def test_default_capacity(self):
        # Arrange
        battery_1 = Battery(70, 0.2)

        # Act
        #battery_1.travel_distance(0)
        
        # Assert
        self.assertEqual(battery_1.capacity_left, 70)
        self.assertEqual(battery_1.life, 100)
    
    def test_driving_large_capacity(self):
        # Arrange
        battery_2 = Battery(60, 0.2)

        # Act
        battery_2.travel_distance(30)

        # Assert
        self.assertEqual(battery_2.capacity_left, 54)
        self.assertEqual(battery_2.life, 90)
    
    def test_driving_half_capacity(self):
        # Arrange
        battery_3 = Battery(50, 0.2)

        # Act
        battery_3.travel_distance(125)

        # Assert
        self.assertEqual(battery_3.capacity_left, 25)
        self.assertEqual(battery_3.life, 50)
    
    def test_driving_low_capacity(self):
        # Arrange
        battery_4 = Battery(40, 0.2)

        # Act
        battery_4.travel_distance(180)

        # Assert
        self.assertEqual(battery_4.capacity_left, 4)
        self.assertEqual(battery_4.life, 10)
    
    def test_recharge(self):
        # Arrange
        battery_5 = Battery(30, 0.2)

        # Act
        battery_5.travel_distance(150)

        # Assert
        self.assertEqual(battery_5.capacity_left, 0)
        self.assertEqual(battery_5.life, 0)

        # Arrange
        battery_5.charge()

        # Assert
        self.assertEqual(battery_5.capacity_left, 30)
        self.assertEqual(battery_5.life, 100)
       

    def test_drive_charge_drive(self):
        # Arrange
        battery_5 = Battery(30, 0.2)

        # Act
        battery_5.travel_distance(150)

        # Arrange
        battery_5.charge()

        # Act
        battery_5.travel_distance(80)

        # Assert
        self.assertEqual(battery_5.capacity_left, 14)
        self.assertAlmostEqual(battery_5.life, 46.66667, places=5)
        


unittest.main()
#battery_1 = Battery.traveled_distance(25)