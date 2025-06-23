#from factories.gas_car_factory import GasCarFactory, GasCarAssemblyLine
#from factories.build_specification import BuildSpecification

class Company():
    def __init__(self, name):      
        self.name = name 
        self.fleet = []
    
    def build_fleet(self, car_factory, build_specifications):
        number_of_cars = len(build_specifications)
        # build_specifications = [
        #     BuildSpecification(),
        #     BuildSpecification(),
        #     BuildSpecification(),
        #     BuildSpecification(),
        #     BuildSpecification()
        # ]

        # build_specifications[0].make = 'Toyota'
        # build_specifications[0].model = 'Corolla'
        # build_specifications[0].year = 2017

        # build_specifications[0].make = 'Honda'
        # build_specifications[0].model = 'Civic'
        # build_specifications[0].year = 2019

        # build_specifications[0].make = 'Hyundai'
        # build_specifications[0].model = 'Elantra'
        # build_specifications[0].year = 2021

        # build_specifications[0].make = 'Nissan'
        # build_specifications[0].model = 'Versa'
        # build_specifications[0].year = 2023

        # build_specifications[0].make = 'Volkswagen'
        # build_specifications[0].model = 'Jetta'
        # build_specifications[0].year = 2025

        for i in range(number_of_cars):
            spec = build_specifications[i]
            car = car_factory.build_gas_car(spec)
            self.fleet.append(car)

        return self.fleet    