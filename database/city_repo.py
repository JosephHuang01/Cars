import pyodbc
from components.shape import ShapeSpecification
from components.position import Position

class CityRepo():
    def __init__(self):
        self.conn = self.__get_connection()

    def __get_connection(self):
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=localhost;'
            'DATABASE=CarExplorer;'
            'Trusted_Connection=yes;'
        )
        return conn

    def get_city_specs(self):
        city_specs = []
        cursor = self.conn.cursor()
        cursor.execute("select * from game.Cities")
        for row in cursor.fetchall():
            # foreground_color = [int(x) for x in row.ForegroundColor.split(',')]
            # background_color = [int(x) for x in row.BackgroundColor.split(',')]
            foreground_color = tuple(int(x) for x in row.ForegroundColor.split(','))
            background_color = tuple(int(x) for x in row.BackgroundColor.split(','))
            
            city_shape_spec = ShapeSpecification(
                # row.Name,
                # row.Type,
                # Position(row.PositionX, row.PositionY),
                # row.Width,
                # row.Length,
                # foreground_color,
                # background_color
                )
            city_shape_spec.name = row.Name
            city_shape_spec.type = row.Type
            city_shape_spec.position = Position(row.PositionX, row.PositionY)
            city_shape_spec.width = row.Width
            city_shape_spec.length = row.Length
            city_shape_spec.bg_color = background_color
            city_shape_spec.fg_color = foreground_color
            #city_spec = City(self.screen, self.pygame, shape_spec)
            # city = {
            #     'CityID': row.CityID,
            #     'Width': row.Width,
            #     'Length': row.Length,
            #     'Name': row.Name,
            #     'Type': row.Type,
            #     'PositionX': row.PositionX,
            #     'PositionY': row.PositionY,
            #     'BackgroundColor': row.BackgroundColor,
            #     'ForegroundColor': row.ForegroundColor
            # }
            city_specs.append(city_shape_spec)
        #self.conn.commit()
        return city_specs

    #def add_cities(self, CityID, ScreenWidth, ScreenLength, Pygame, Name, Type, PositionX, PositionY, BackgroundColor, Foreground Color):