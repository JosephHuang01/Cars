import pyodbc

class BaseRepo():
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
    
    def get_specs(self):
        pass