from components.shape import Shape, ShapeSpecification
from components.map import Map
from database.city_repo import CityRepo
from components.city import City
from components.position import Position
from database.road_repo import RoadRepo
from components.road import Road
from database.car_repo import CarRepo
from components.car import Car

class Builder():
    def __init__(self, screen, pygame):
        self.screen = screen
        self.pygame = pygame
        self.screen_size = self.screen.get_size()

    def build(self):
        #ai_settings = Settings()
        shape_spec_map = ShapeSpecification()
        shape_spec_map.name = 'Game Map'
        shape_spec_map.type = 'map'
        screen_width, screen_height = self.screen_size
        shape_spec_map.width = screen_width - 50
        shape_spec_map.length = screen_height - 50
    
        self.grid_map = Map(self.screen, self.pygame, shape_spec_map)
        self.grid_map.center_position()

        city_specs = CityRepo().get_specs()
        cities = [] # CityRepo(screen, pygame).get_cities()
        for city_spec in city_specs:
            cities.append(City(self.screen, self.pygame, city_spec))
        for city in cities:
            self.grid_map.add_city(city)

        road_specs = RoadRepo().get_specs()
        roads = []
        for road_spec in road_specs:
            roads.append(Road(self.screen, self.pygame, road_spec))
        for road in roads:
            self.grid_map.add_road(road)

        car_specs = CarRepo().get_specs()
        cars = []
        for car_spec in car_specs:
            cars.append(Car(self.screen, self.pygame, car_spec))
        for car in cars:
            self.grid_map.add_car(car)
        
        self.cars = cars
        for car in cars:
            car.set_destination(Position(200, 200))

        # self.cars[0].set_destination(Position(200, 200))
        # self.cars[0].update()
        # self.cars[0].show()

        #self.demo_shape = Shape(self.screen, self.pygame, ShapeSpecification())
        # self.demo_shape.drawing_points = [Position(125, 125), Position(650, 650), Position(650, 125), Position(125, 125)]
        #self.demo_shape.drawing_points = [Position(700, 400), Position(800, 500), Position(750, 600), Position(650, 600)
                                     #, Position(600, 500), Position(700, 400)]
        # self.demo_shape.drawing_points = [Position(75, 125), Position(75, 375), Position(100, 375), Position(100, 125)
        #                                   , Position(75, 125)]
        #self.demo_car = Shape(self.screen, self.pygame, ShapeSpecification())

    def show(self):
        self.grid_map.show()
        self.grid_map.show_cities()
        #self.demo_shape.show()
        #self.demo_car.show()
        self.grid_map.show_roads()
        self.grid_map.show_cars()