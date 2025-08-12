class Company():
    def __init__(self, name):      
        self.name = name 
        self.fleet = []
    
    def build_fleet(self, car_factory, build_specifications):
        number_of_cars = len(build_specifications)

        for i in range(number_of_cars):
            spec = build_specifications[i]
            car = car_factory.build_gas_car(spec)
            self.fleet.append(car)

        return self.fleet    