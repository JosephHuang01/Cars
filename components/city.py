from components.position import Position

class City():
    cities = []

    def __init__(self, name, x, y):
        self.name = name
        self.position = Position(x, y)
        City.cities.append(self)

    def get_popular_cities(self):
        return City.cities