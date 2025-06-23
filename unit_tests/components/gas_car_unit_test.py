import unittest

from components.gas_car import GasCar

class TestGasCar(unittest.TestCase):

    def test_drive_forward_60(self):
        # Arrange
        test_my_gas_car_1 = GasCar('Toyota', 'Corolla', 2017, 15, 0.05)

        # Act
        test_my_gas_car_1.travel_distance("forward", 60)

        # Assert
        self.assertEqual(test_my_gas_car_1.miles_drove, 60)
        self.assertEqual(test_my_gas_car_1.gas_tank.capacity_left, 12)
        self.assertEqual(test_my_gas_car_1.gas_tank.percentage, 80)
        self.assertEqual(test_my_gas_car_1.direction, "forward")
        # add position assert

    def test_drive_foward_60_then_turn_left_120(self):
        # Arrange
        test_my_gas_car_1 = GasCar('Toyota', 'Corolla', 2017, 15, 0.05)
        test_my_gas_car_1.travel_distance("forward", 60)
       
        # Act
        test_my_gas_car_1.travel_distance("left", 120)

        # Assert
        self.assertEqual(test_my_gas_car_1.miles_drove, 60)
        self.assertEqual(test_my_gas_car_1.gas_tank.capacity_left, 12)
        self.assertEqual(test_my_gas_car_1.gas_tank.percentage, 80)
        self.assertEqual(test_my_gas_car_1.direction, "left")
    
    def test_drive_reverse_turn(self):
        # Arrange
        test_my_gas_car_1 = GasCar('Toyota', 'Corolla', 2017, 15, 0.05)
        test_my_gas_car_1.travel_distance("forward", 60)
        test_my_gas_car_1.travel_distance("left", 120)

        # Act
        test_my_gas_car_1.travel_distance("right", 120)

        # Assert
        self.assertEqual(test_my_gas_car_1.miles_drove, 60)
        self.assertEqual(test_my_gas_car_1.gas_tank.capacity_left, 12)
        self.assertEqual(test_my_gas_car_1.gas_tank.percentage, 0)
        self.assertEqual(test_my_gas_car_1.direction, "right")

        #test_my_gas_car_1.fill_gas(0.5)
        #self.assertEqual(test_my_gas_car_1.capacity, 15)
    
    # def test_driving_with_tank_half_full(self):
    #     test_gas_tank_3 = GasCar('Hyundai', 'Kona', 2023)
    #     test_gas_tank_3.move_with_gas(5, "left", 4)
    #     test_gas_tank_3.turn_left(4)
    #     self.assertEqual(test_gas_tank_3.read_odometer(), 4)

    # def test_refuel(self):
    #     test_gas_tank_5 = GasCar('Honda', 'Civic', 2020)
    #     test_gas_tank_5.move_with_gas(10, "backward", 10)
    #     test_gas_tank_5.drive_backward(6)
    #     test_gas_tank_5.turn_left(4)
    #     self.assertEqual(test_gas_tank_5.read_odometer(), 10)

if __name__ == '__main__':
    unittest.main()