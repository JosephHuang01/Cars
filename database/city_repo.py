import pyodbc
from components.city import City
from components.shape import ShapeSpecification
from components.position import Position

class CityRepo():
    def __init__(self, screen, pygame):
        self.conn = self.__get_connection()
        self.screen = screen
        self.pygame = pygame

    def __get_connection(self):
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=localhost;'
            'DATABASE=CarExplorer;'
            'Trusted_Connection=yes;'
        )
        return conn
    
    def get_cities(self):
        cities = []
        cursor = self.conn.cursor()
        cursor.execute("select * from game.Cities")
        for row in cursor.fetchall():
            # foreground_color = [int(x) for x in row.ForegroundColor.split(',')]
            # background_color = [int(x) for x in row.BackgroundColor.split(',')]
            foreground_color = tuple(int(x) for x in row.ForegroundColor.split(','))
            background_color = tuple(int(x) for x in row.BackgroundColor.split(','))
            
            shape_spec = ShapeSpecification(
                # row.Name,
                # row.Type,
                # Position(row.PositionX, row.PositionY),
                # row.Width,
                # row.Length,
                # foreground_color,
                # background_color
                )
            shape_spec.name = row.Name
            shape_spec.type = row.Type
            shape_spec.position = Position(row.PositionX, row.PositionY)
            shape_spec.width = row.Width
            shape_spec.length = row.Length
            shape_spec.bg_color = background_color
            shape_spec.fg_color = foreground_color
            city1 = City(self.screen, self.pygame, shape_spec)
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
            cities.append(city1)
        #self.conn.commit()
        return cities

    #def add_cities(self, CityID, ScreenWidth, ScreenLength, Pygame, Name, Type, PositionX, PositionY, BackgroundColor, Foreground Color):
