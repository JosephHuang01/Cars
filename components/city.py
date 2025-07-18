from components.shape import Shape, ShapeSpecification

class City(Shape):
    def __init__(self, screen, pygame, shape_spec):
        super().__init__(screen, pygame, shape_spec)
        self.map_grid = map

    def get_popular_cities(self):
        # return [City(self.screen, self.pygame, self.shape_spec_map.type,
        #             Position(100, 100), self.shape_spec_map.width, self.shape_spec_map.length,
        #             CommonGameColor.BLUE, CommonGameColor.RED, self.map_grid),
        #         City(self.screen, self.pygame, self.shape_spec_map, 'city'
        #              , Position(600, 100), 75, 75
        #              , CommonGameColor.BLUE, CommonGameColor.RED, self.map_grid),
        #         City(self.screen, self.pygame, self.shape_spec_map, self.shape_spec_map.type
        #              , Position(100, 400), 75, 75
        #              , CommonGameColor.BLUE, CommonGameColor.RED, self.map_grid),
        #         City(self.screen, self.pygame, self.shape_spec_map, self.shape_spec_map.type
        #              , Position(500, 500), 75, 75
        #              , CommonGameColor.BLUE, CommonGameColor.RED, self.map_grid)]

        # return [City(self.screen, self.pygame, ShapeSpecification('Seattle', 'city', Position(100, 100), 75, 75
        #                                                           , CommonGameColor.BLUE, CommonGameColor.RED)),
        #         City(self.screen, self.pygame, ShapeSpecification('New York', 'city', Position(1400, 50), 75, 75,
        #                                                           CommonGameColor.BLACK, CommonGameColor.BLUE)),
        #         City(self.screen, self.pygame, ShapeSpecification('Los Angeles', 'city', Position(100, 550), 75, 75,
        #                                                           CommonGameColor.GREEN, CommonGameColor.WHITE)),
        #         City(self.screen, self.pygame, ShapeSpecification('Atlanta', 'city', Position(1250, 550), 75, 75,
        #                                                           CommonGameColor.RED, CommonGameColor.BLACK))]
        return [City(self.screen, self.pygame, ShapeSpecification())]
    
    def show(self):
        super().show()
        self.draw_text_on_rectangle(self.name, self.position, self.width, self.length)
        #Shape.draw_text_on_rectangle(self.name, self.position, self.width, self.length)