import pyodbc
print ('pyodbc ok!')

import sys
from datetime import datetime, timedelta
from components.car import Car, Position

class CarExplorer():
    def __init__(self):
        self.conn = self.__get_connection()

    def __get_connection(self):
        # Connect to SQL Server
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=localhost;'      # e.g., 'localhost\\SQLEXPRESS' or '192.168.1.100'
            'DATABASE=CarExplorer;'  # e.g., 'insurance_db'
            #'UID=YOUR_USERNAME;'            # If using SQL Auth (not needed for Windows Auth)
            #'PWD=YOUR_PASSWORD;'            # If using SQL Auth
            # For Windows Authentication:
            'Trusted_Connection=yes;'
        )
        return conn
    
    def get_one_car(self):
        cursor = self.conn.cursor()
        cursor.execute("select top 5 * from game.Cars")

        first_row = cursor.fetchone()
        if first_row:
            car_id = first_row.CarId
            car_make = first_row.Make
            car_model = first_row.Model
            car_year = first_row.Year

        car_a = Car(car_make, car_model, car_year)
        car_a.car_id = car_id
        return car_a

    def get_last_trip_position(self, car_id):
        cursor = self.conn.cursor()        
        cursor.execute("select * from game.Trips where CarID = ? ORDER BY EndDateTime DESC", car_id)
        row_one = cursor.fetchone()
        
        if row_one:
            trip_id = row_one.TripId
            start_x = row_one.StartX
            start_y = row_one.StartY
            end_x = row_one.EndX
            end_y = row_one.EndY
            start_date_time = row_one.StartDateTime
            end_date_time = row_one.EndDateTime

        return Position(end_x, end_y)
    
    def save_trip(self, car_id, start_position_x, start_position_y, end_position_x, end_position_y, start_date, end_date):
        cursor = self.conn.cursor()
        #end_date = start_date + timedelta(minutes=3)
        cursor.execute("insert into game.Trips (CarId, StartX, StartY, EndX, EndY, StartDateTime, EndDateTime)"
               "values (?, ?, ?, ?, ?, ?, ?)",
               (car_id, start_position_x, start_position_y, end_position_x, end_position_y, start_date, end_date))
        self.conn.commit()
        return end_date