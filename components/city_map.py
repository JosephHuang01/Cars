class CityMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.roads = set()
        self.buildings = set()

    def add_road(self, x, y):
        self.roads.add((x, y))

    def add_building(self, x, y):
        self.buildings.add((x, y))

    def is_road(self, x, y):
        return (x, y) in self.roads

    def is_blocked(self, x, y):
        return (x, y) in self.buildings