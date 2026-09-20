CREATE SCHEMA game;
GO

CREATE TABLE game.Cars (
    CarId INT IDENTITY(1,1) PRIMARY KEY,
    Make VARCHAR(50) NOT NULL,
    Model VARCHAR(50) NOT NULL,
    [Year] INT NOT NULL
)
GO

CREATE TABLE game.Trips (
    TripId INT IDENTITY(1,1) PRIMARY KEY,
    CarId INT NOT NULL,
    FOREIGN KEY (CarId) REFERENCES game.Cars(CarId),
    StartX FLOAT NOT NULL,
    StartY FLOAT NOT NULL,
    EndX FLOAT NOT NULL,
    EndY FLOAT NOT NULL,
    StartDateTime DATETIME NOT NULL,
    EndDateTime DATETIME NOT NULL
)

INSERT INTO game.Cars (Make, Model, Year) VALUES
('Toyota', 'Corolla', 2017),
('Ford', 'Mustang', 2020),
('Honda', 'Civic', 2024)

INSERT INTO game.Trips (CarId, StartX, StartY, EndX, EndY, StartDateTime, EndDateTime) VALUES
(1, 3.5, 0.5, 6.5, 5.5, '2025-06-28 10:15:23', '2025-06-28 10:31:47'),
(2, 6.5, 5.5, 1.5, 2.5, '2025-06-28 10:32:01', '2025-06-28 10:48:17'),
(3, 1.5, 2.5, 0.5, 6.5, '2025-06-28 10:48:40', '2025-06-28 10:58:52');

SELECT * FROM game.Cars
SELECT * FROM game.Trips