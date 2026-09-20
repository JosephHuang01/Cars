from database.base_repo import BaseRepo
from components.shape import ShapeSpecification
from components.position import Position

class CarRepo(BaseRepo):
    def __init__(self):
        super().__init__()
       
    def get_specs(self):
        car_specs = []
        cursor = self.conn.cursor()
        cursor.execute("select * from game.Car")
        for row in cursor.fetchall():
            foreground_color = tuple(int(x) for x in row.ForegroundColor.split(','))
            background_color = tuple(int(x) for x in row.BackgroundColor.split(','))

            car_shape_spec = ShapeSpecification()
            car_shape_spec.name = row.Name
            car_shape_spec.type = row.Type
            car_shape_spec.position = Position(row.PositionX, row.PositionY)
            car_shape_spec.width = row.Width
            car_shape_spec.length = row.Length
            car_shape_spec.bg_color = background_color
            car_shape_spec.fg_color = foreground_color
            car_specs.append(car_shape_spec)
        return car_specs