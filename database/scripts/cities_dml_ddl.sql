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
           50,
           50,
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
           50,
           375,
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
           1290,
           570,
           '255,0,0',
           '0,0,0')
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
           'Billings',
           'city',
           725,
           125,
           '255,0,0',
           '0,0,0')
GO


drop table game.cities

CREATE TABLE game.Cities (
	CityID INT IDENTITY(1,1) PRIMARY KEY,
	Width INT NOT NULL,
	[Length] INT NOT NULL,
	[Name] VARCHAR(50) NOT NULL,
	[Type] VARCHAR(10) NOT NULL,
	PositionX INT NOT NULL,
	PositionY INT NOT NULL,
	BackgroundColor VARCHAR(15) NOT NULL,
	ForegroundColor VARCHAR(15) NOT NULL
)

SELECT * FROM game.Cities

DROP TABLE game.Roads

CREATE TABLE game.Roads (
	RoadID INT IDENTITY(1,1) PRIMARY KEY,
	Width INT NOT NULL,
	[Length] INT NOT NULL,
	[Type] VARCHAR(10) NOT NULL,
	PositionX INT NOT NULL,
	PositionY INT NOT NULL,
	BackgroundColor VARCHAR(15) NOT NULL,
	ForegroundColor VARCHAR(15) NOT NULL
)

SELECT * FROM game.Roads

USE [CarExplorer]
GO

INSERT INTO [game].[Roads]
           ([Width]
           ,[Length]
           ,[Type]
           ,[PositionX]
           ,[PositionY]
           ,[BackgroundColor]
           ,[ForegroundColor])
     VALUES
           (25,
           -200,
           'road',
           675,
           400,
           '0,0,0',
           '255,255,255')
GO