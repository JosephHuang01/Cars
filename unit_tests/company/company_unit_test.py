import unittest
from company.company import Company
from factories.gas_car_factory import *
from factories.build_specification import BuildSpecification

class TestCompanyFleet(unittest.TestCase):
    def test_five_car_list(self):
        # Arrange
        company = Company('Car Explorer')
        gas_car_factory = GasCarFactory()
        build_specifications = [BuildSpecification() for i in range(5)]
        
        # Act
        build_specifications[0].make = 'Toyota'
        build_specifications[0].model = 'Corolla'
        build_specifications[0].year = 2017

        build_specifications[1].make = 'Honda'
        build_specifications[1].model = 'Civic'
        build_specifications[1].year = 2019

        build_specifications[2].make = 'Hyundai'
        build_specifications[2].model = 'Elantra'
        build_specifications[2].year = 2021

        build_specifications[3].make = 'Nissan'
        build_specifications[3].model = 'Versa'
        build_specifications[3].year = 2023

        build_specifications[4].make = 'Volkswagen'
        build_specifications[4].model = 'Jetta'
        build_specifications[4].year = 2025
        
        fleet = company.build_fleet(gas_car_factory, build_specifications)

        # Assert
        self.assertEqual(len(fleet), 5)

        self.assertEqual(fleet[0].make, 'Toyota')
        self.assertEqual(fleet[0].model, 'Corolla')
        self.assertEqual(fleet[0].year, 2017)

        self.assertEqual(fleet[1].make, 'Honda')
        self.assertEqual(fleet[1].model, 'Civic')
        self.assertEqual(fleet[1].year, 2019)

        self.assertEqual(fleet[2].make, 'Hyundai')
        self.assertEqual(fleet[2].model, 'Elantra')
        self.assertEqual(fleet[2].year, 2021)

        self.assertEqual(fleet[3].make, 'Nissan')
        self.assertEqual(fleet[3].model, 'Versa')
        self.assertEqual(fleet[3].year, 2023)

        self.assertEqual(fleet[4].make, 'Volkswagen')
        self.assertEqual(fleet[4].model, 'Jetta')
        self.assertEqual(fleet[4].year, 2025)

unittest.main()