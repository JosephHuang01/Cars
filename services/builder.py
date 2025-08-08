from components.shape import ShapeSpecification
from components.map import Map
from database.city_repo import CityRepo
from components.city import City
from database.road_repo import RoadRepo
from components.road import Road
from database.car_repo import CarRepo
from components.car import Car

class Builder():
    def __init__(self, screen, pygame):
        self.screen = screen
        self.pygame = pygame
        self.screen_size = self.screen.get_size()
        self.cars = []
        self.roads = []
        self.cities = []

    def get_map(self):
        return self.grid_map
    
    def build(self):
        shape_spec_map = ShapeSpecification()
        shape_spec_map.name = 'Game Map'
        shape_spec_map.type = 'map'
        screen_width, screen_height = self.screen_size
        shape_spec_map.width = screen_width - 50
        shape_spec_map.length = screen_height - 50
    
        self.grid_map = Map(self.screen, self.pygame, shape_spec_map)
        self.grid_map.center_position()

        city_specs = CityRepo().get_specs()
        self.cities = [] # CityRepo(screen, pygame).get_cities()
        for city_spec in city_specs:
            self.cities.append(City(self.screen, self.pygame, city_spec))
        for city in self.cities:
            self.grid_map.add_city(city)

        road_specs = RoadRepo().get_specs()
        self.roads = []
        for road_spec in road_specs:
            self.roads.append(Road(self.screen, self.pygame, road_spec))
        for road in self.roads:
            self.grid_map.add_road(road)

        car_specs = CarRepo().get_specs()
        self.cars = []
        for car_spec in car_specs:
            self.cars.append(Car(self.screen, self.pygame, car_spec))
        for car in self.cars:
            self.grid_map.add_car(car)
    
    def show(self):
        self.grid_map.show()
        self.grid_map.show_cities()
        #self.demo_shape.show()
        #self.demo_car.show()
        self.grid_map.show_roads()
        self.grid_map.show_cars()