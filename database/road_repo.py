from database.base_repo import BaseRepo
from components.shape import ShapeSpecification
from components.position import Position

class RoadRepo(BaseRepo):
    def __init__(self):
        super().__init__()

    def get_specs(self):
        road_specs = []
        cursor = self.conn.cursor()
        cursor.execute("select * from game.Roads")
        for row in cursor.fetchall():
            foreground_color = tuple(int(x) for x in row.ForegroundColor.split(','))
            background_color = tuple(int(x) for x in row.BackgroundColor.split(','))

            road_shape_spec = ShapeSpecification()
            road_shape_spec.type = row.Type
            road_shape_spec.position = Position(row.PositionX, row.PositionY)
            road_shape_spec.width = row.Width
            road_shape_spec.length = row.Length
            road_shape_spec.bg_color = background_color
            road_shape_spec.fg_color = foreground_color
            road_specs.append(road_shape_spec)
        return road_specs