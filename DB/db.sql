CREATE DATABASE ESTATE
GO

USE ESTATE;
GO

CREATE TABLE Wlelfare(
        Id INT PRIMARY KEY IDENTITY ,
        WlelfareCode CHAR(150)  NOT NULL UNIQUE ,
        Title NVARCHAR(200) NULL ,
        Icon VARCHAR(350) NULL
    );

CREATE TABLE Category(
    ID INT PRIMARY KEY IDENTITY ,
    CategoryCode CHAR(150) NOT NULL UNIQUE ,
    ParentId INT FOREIGN KEY REFERENCES Category(ID) ,
    Title NVARCHAR(150)
    );

CREATE TABLE Estate(
    ID INT PRIMARY KEY IDENTITY ,
    EstateCode CHAR(150) NOT NULL UNIQUE ,
    Name NVARCHAR(150) NOT NULL ,
    Address NVARCHAR(350) NOT NULL ,
    PhoneNumber CHAR(25) NOT NULL
    );

CREATE TABLE State(
    ID INT PRIMARY KEY IDENTITY ,
    StateCode CHAR(150) NOT NULL UNIQUE ,
    Title NVARCHAR(200)
    );

CREATE TABLE Role(
    ID INT PRIMARY KEY IDENTITY ,
    RoleCode CHAR(150) NOT NULL UNIQUE ,
    Title NVARCHAR(150)
    );


CREATE TABLE [User](
    ID INT PRIMARY KEY IDENTITY ,
    UserCode CHAR(150) NOT NULL UNIQUE ,
    RoleId  INT FOREIGN KEY REFERENCES Role(ID) ON DELETE CASCADE ,
    Name NVARCHAR(200) NULL ,
    Family NVARCHAR(200) NULL ,
    Email CHAR(150) ,
    Password char(100) ,
    );

CREATE TABLE ImageType(
    ID INT PRIMARY KEY IDENTITY ,
    ImageTypeCode CHAR(150) NOT NULL UNIQUE ,
    Title NVARCHAR(200)
    );

CREATE TABLE Image(
    ID INT PRIMARY KEY IDENTITY ,
    ImageTypeId INT FOREIGN KEY REFERENCES ImageType(ID) ON DELETE CASCADE ,
    URL VARCHAR(500)
    );

CREATE TABLE Types(
    ID INT PRIMARY KEY IDENTITY ,
    TypesCode CHAR(150) NOT NULL UNIQUE ,
    Title NVARCHAR(250) ,
    );

CREATE TABLE Feature(
    ID INT PRIMARY KEY IDENTITY ,
    FeatureCode CHAR(150) NOT NULL UNIQUE ,
    Title NVARCHAR(250) ,
    );

CREATE TABLE FeatureType(
    ID INT PRIMARY KEY IDENTITY ,
    FeatureId INT FOREIGN KEY REFERENCES Feature(ID) ON DELETE CASCADE ,
    TypeId INT FOREIGN KEY REFERENCES Types(ID) ON DELETE CASCADE ,
    );

CREATE TABLE Files(
    ID INT PRIMARY KEY IDENTITY ,
    FilesCode CHAR(150) NOT NULL UNIQUE ,
    TypeId INT FOREIGN KEY REFERENCES Types(ID) ON DELETE CASCADE ,
    CategoryId INT FOREIGN KEY REFERENCES Category(ID) ON DELETE CASCADE ,
    EstateId INT FOREIGN KEY REFERENCES Estate(ID) ON DELETE CASCADE  ,
    StateId  INT FOREIGN KEY REFERENCES State(ID) ON DELETE CASCADE  ,
    CreatorId INT FOREIGN KEY REFERENCES [User](ID) ON DELETE CASCADE  ,
    Title NVARCHAR(150) ,
    Laws NVARCHAR(500) ,
    PhoneNumber CHAR(25)
    );

CREATE TABLE FeatureTypeFile(
    FileId INT FOREIGN KEY REFERENCES Files(ID) ON DELETE CASCADE,
    FeatureTypeId INT FOREIGN KEY REFERENCES FeatureType(ID) ON DELETE NO ACTION ,
    Value VARCHAR(150)
);

CREATE TABLE FileImage(
    FileId INT FOREIGN KEY REFERENCES FILES(ID) ON DELETE CASCADE ,
    ImageId INT FOREIGN KEY REFERENCES Image(ID) ON DELETE CASCADE
    );

CREATE TABLE FileWlelfare(
    FileId INT FOREIGN KEY REFERENCES FILES(ID) ON DELETE CASCADE ,
    WlelfareId INT FOREIGN KEY REFERENCES Wlelfare(ID) ON DELETE CASCADE ,
    );

CREATE TABLE FilesReturn(
    FileId INT FOREIGN KEY REFERENCES FILES(ID) ON DELETE CASCADE ,
    Description NVARCHAR(500)
    );




INSERT INTO Wlelfare(WlelfareCode,Title,Icon)
    VALUES  ('PARKING',N'پارکینگ',NULL ),
            ('POOL',N'استخر',null ),
            ('HEATER',N'شوفاژ',NULL ),
            ('COOL',N'کولر',NULL );

INSERT INTO Category(CategoryCode,ParentId,Title)
    VALUES  ('EARTH',null,N'زمین') ,
            ('VILLA',null ,N'ویلا') ,
            ('HOME',null ,N'خانه')  ,
            ('APARTMENT',null ,N'آپارتمان')

INSERT INTO Estate(EstateCode,Name,Address,PhoneNumber)
    VALUES ('EA',N'آسمان',N'تهران',N'09125478923'),
           ('EB',N'بهمن',N'تهران',N'09125864215'),
           ('EC',N'سیراف',N'تهران',N'09127531568');

INSERT INTO State(StateCode,Title)
    VALUES  ('AC',N'فعال'),
            ('DAC',N'غیرفعال'),
            ('WAC',N'در انتطار تایید'),
            ('BL',N'مسدود');

INSERT INTO Role(RoleCode,Title)
    VALUES ('AD',N'ادمین'),
           ('US',N'کاربر');

INSERT INTO ImageType(ImageTypeCode,Title)
    VALUES ('GALERY',N'گالری'),
           ('PRO',N'پروفایل');

INSERT INTO Feature(FeatureCode,Title)
    VALUES ('MONTHRENT',N'اجاره ماهیانه'),
           ('DAYRENT',N'اجاره روزانه') ,
           ('MORTAGAGE',N'قیمت رهن') ,
           ('PRICE',N'قیمت');

INSERT INTO Types(TypesCode,Title)
    VALUES ('RENT',N'اجاره'),
           ('BUY',N'خرید'),
           ('SALE',N'فروش'),
           ('DAYRENT',N'اجاره روزانه'),
           ('MORTAGAGE',N'رهن')

INSERT  INTO FeatureType(FeatureId,TypeId)
    VALUES  (1,1),(3,1),(4,2),
            (4,3),(2,4),(3,5);
