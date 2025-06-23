import unittest

from components.hybrid_car import HybridCar

class TestHybridCar(unittest.TestCase):

    def test_default_capacity(self):
        test_hybrid_engine_1 = HybridCar('Alfa Romeo', 'Tonale', 2025, 15, 70)
        test_hybrid_engine_1.move_with_gas(15, "left", 6)
        test_hybrid_engine_1.drive_forward(3)
        test_hybrid_engine_1.turn_left(3)
        self.assertEqual(test_hybrid_engine_1.read_odometer(), 6)
    
    def test_half_capacity_charge_fuel(self):
        test_hybrid_engine_3 = HybridCar('Toyota', 'Sienna Hybrid', 2023, 7.5, 85)
        test_hybrid_engine_3.move_with_gas(7.5, "forward", 10)
        test_hybrid_engine_3.drive_forward(10)
        self.assertEqual(test_hybrid_engine_3.read_odometer(), 10)
    
    def test_recharge_refuel(self):
        test_hybrid_engine_5 = HybridCar('BMW', 'X5', 2024, 0, 0)
        test_hybrid_engine_5.move_with_gas(0, "backward", 8)
        test_hybrid_engine_5.drive_backward(6)
        test_hybrid_engine_5.turn_right(2)
        self.assertEqual(test_hybrid_engine_5.read_odometer(), 8)

unittest.main()