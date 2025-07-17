CREATE TABLE game.Cities (
	CityID INT IDENTITY(1,1) PRIMARY KEY,
	Width INT NOT NULL,
	[Length] INT NOT NULL,
	Pygame VARCHAR(100) NOT NULL,
	[Name] VARCHAR(50) NOT NULL,
	[Type] VARCHAR(10) NOT NULL,
	PositionX INT NOT NULL,
	PositionY INT NOT NULL,
	BackgroundColor VARCHAR(15) NOT NULL,
	ForegroundColor VARCHAR(15) NOT NULL
)

SELECT * FROM game.Cities

USE [CarExplorer]
GO

INSERT INTO [game].[Cities]
           ([Width]
           ,[Length]
           ,[Name]
           ,[Type]
           ,[PositionX]
           ,[PositionY]
           ,[BackgroundColor]
           ,[ForegroundColor])
     VALUES
           (75,
           75,
           'Seattle',
           'city',
           100,
           100,
           '0,0,255',
           '255,0,0')
GO

INSERT INTO [game].[Cities]
           ([Width]
           ,[Length]
           ,[Name]
           ,[Type]
           ,[PositionX]
           ,[PositionY]
           ,[BackgroundColor]
           ,[ForegroundColor])
     VALUES
           (75,
           75,
           'New York',
           'city',
           1400,
           50,
           '0,0,0',
           '0,0,255')
GO

INSERT INTO [game].[Cities]
           ([Width]
           ,[Length]
           ,[Name]
           ,[Type]
           ,[PositionX]
           ,[PositionY]
           ,[BackgroundColor]
           ,[ForegroundColor])
     VALUES
           (75,
           75,
           'Los Angeles',
           'city',
           100,
           550,
           '0,128,0',
           '255,255,255')
GO

INSERT INTO [game].[Cities]
           ([Width]
           ,[Length]
           ,[Name]
           ,[Type]
           ,[PositionX]
           ,[PositionY]
           ,[BackgroundColor]
           ,[ForegroundColor])
     VALUES
           (75,
           75,
           'Atlanta',
           'city',
           1250,
           550,
           '255,0,0',
           '0,0,0')
GO