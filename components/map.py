from components.shape import Shape

class Map(Shape):
    def __init__(self, screen, pygame, shape_spec):
        super().__init__(screen, pygame, shape_spec)
        if self.screen is not None:
            self.screen_size = self.screen.get_size()
        if self.pygame is not None:
            self.font = pygame.font.SysFont(None, 15)
        self.cities = []
        self.cars = []
        self.roads = []
    
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
    
    def add_road(self, road):
        self.roads.append(road)
    
    def show_roads(self):
        for road in self.roads:
            road.show()
    
    def is_position_on_road(self, position):
        is_on_road = False
        for road in self.roads:
            if road.is_inside_the_shape(position):
                is_on_road = True
                break

        return is_on_road
    
    def is_position_on_city(self, position):
        is_on_city = False
        for city in self.cities:
            if city.is_inside_the_shape(position):
                is_on_city = True
                break
        
        return is_on_city