from database.base_repo import BaseRepo
from components.position import Position
from components.shape import ShapeSpecification

class CityRepo(BaseRepo):
    def __init__(self):
        super().__init__()

    def get_specs(self):
        city_specs = []
        cursor = self.conn.cursor()
        cursor.execute("select * from game.Cities")
        for row in cursor.fetchall():
            foreground_color = tuple(int(x) for x in row.ForegroundColor.split(','))
            background_color = tuple(int(x) for x in row.BackgroundColor.split(','))

            city_shape_spec = ShapeSpecification()
            city_shape_spec.name = row.Name
            city_shape_spec.type = row.Type
            city_shape_spec.position = Position(row.PositionX, row.PositionY)
            city_shape_spec.width = row.Width
            city_shape_spec.length = row.Length
            city_shape_spec.bg_color = background_color
            city_shape_spec.fg_color = foreground_color
            city_specs.append(city_shape_spec)
        return city_specs