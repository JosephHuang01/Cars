from components.shape import Shape

class Map(Shape):
    def __init__(self, screen, pygame, shape_spec):
        super().__init__(screen, pygame, shape_spec)
        self.cities = []
        self.cars = []
    
    def add_city(self, city):
        self.cities.append(city)

    def show_cities(self):
        for city in self.cities:
            city.show()
    
    def add_car(self, car):
        self.cars.append(car)
    
    def show_cars(self):
        for car in self.cars:
            car.show()