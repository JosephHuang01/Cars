class Position():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def get_distance(self, position):
        x_distance = self.x - position.x
        y_distance = self.y - position.y
        return (x_distance * x_distance + y_distance * y_distance) ** 0.5
    
    def get_positions_in_four_directions(self, distance):
        return[
            Position(self.x + distance, self.y),
            Position(self.x - 1000, self.y),
            Position(self.x, self.y + 1000),
            Position(self.x, self.y - 1000)
        ]

    def find_shortest_distance_to_position(self, positions):
        shortest_position = Position(3000, 3000)
        shortest_distance = 6000
        for position in positions:
            distance = self.get_distance(position)
            if distance <= shortest_distance:
                shortest_distance  = distance
                shortest_position = position

        return shortest_position
    
    def is_same_position(self, position):
        return self.x == position.x and self.y == position.y