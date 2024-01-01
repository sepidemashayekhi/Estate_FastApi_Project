from conection import SqlConnection

DBconect = SqlConnection()

Wlelfare = """
    CREATE TABLE Wlelfare(
        Id INT PRIMARY KEY IDENTITY ,
        WlelfareCode CHAR(150)  NOT NULL UNIQUE ,
        Title NVARCHAR(200) NULL ,
        Icon VARCHAR(350) NOT NULL        
    )
    
"""

Category = """
    CREATE TABLE Category(
    ID INT PRIMARY KEY IDENTITY ,
    CategoryCode CHAR(150) NOT NULL UNIQUE ,
    ParentId INT FOREIGN KEY REFERENCES Category(ID) ,
    Title CHAR(150)
    )
    
"""

Estate = """
    CREATE TABLE Estate(
    ID INT PRIMARY KEY IDENTITY ,
    EstateCode CHAR(150) NOT NULL UNIQUE ,
    Name NVARCHAR(150) NOT NULL ,
    Address NVARCHAR(350) NOT NULL ,
    PhoneNumber CHAR(25) NOT NULL 
    )
    
"""

State = """
    CREATE TABLE State(
    ID INT PRIMARY KEY IDENTITY ,
    StateCode CHAR(150) NOT NULL UNIQUE ,
    Title NVARCHAR(200)
    )
    
"""

Role = """
    CREATE TABLE Role(
    ID INT PRIMARY KEY IDENTITY ,
    RoleCode CHAR(150) NOT NULL UNIQUE ,
    Title NVARCHAR(150)
    )
    
"""

User = """
    CREATE TABLE [User](
    ID INT PRIMARY KEY IDENTITY ,
    UserCode CHAR(150) NOT NULL UNIQUE ,
    RoleId  INT FOREIGN KEY REFERENCES Role(ID) ON DELETE CASCADE ,
    Name NVARCHAR(200) NULL ,
    Family NVARCHAR(200) NULL ,
    Email CHAR(150) ,
    Password char(100) ,
    )
    
"""

ImageType = """
    CREATE TABLE ImageType(
    ID INT PRIMARY KEY IDENTITY ,
    ImageTypeCode CHAR(150) NOT NULL UNIQUE ,
    Title NVARCHAR(200)
    )
    
"""

Image = """
    CREATE TABLE Image(
    ID INT PRIMARY KEY IDENTITY ,
    ImageTypeId INT FOREIGN KEY REFERENCES ImageType(ID) ON DELETE CASCADE ,
    URL VARCHAR(500) 
    )
"""

Types = """
    CREATE TABLE Types(
    ID INT PRIMARY KEY IDENTITY ,
    TypesCode CHAR(150) NOT NULL UNIQUE ,
    Title NVARCHAR(250) ,
    )
"""

Feature = """
    CREATE TABLE Feature(
    ID INT PRIMARY KEY IDENTITY ,
    FeatureCode CHAR(150) NOT NULL UNIQUE ,
    Title NVARCHAR(250) ,
    )
"""

FeatureType = """
    CREATE TABLE FeatureType(
    FeatureId INT FOREIGN KEY REFERENCES Feature(ID) ON DELETE CASCADE ,
    TypeId INT FOREIGN KEY REFERENCES Types(ID) ON DELETE CASCADE ,
    Value char(150)
    )
    
"""

Files = """
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
    )
    
"""


FileImage = """
    CREATE TABLE FileImage(
    FileId INT FOREIGN KEY REFERENCES FILES(ID) ON DELETE CASCADE ,
    ImageId INT FOREIGN KEY REFERENCES Image(ID) ON DELETE CASCADE
    )
    
"""

FileWlelfare = """
    CREATE TABLE FileWlelfare(
    FileId INT FOREIGN KEY REFERENCES FILES(ID) ON DELETE CASCADE ,
    WlelfareId INT FOREIGN KEY REFERENCES Wlelfare(ID) ON DELETE CASCADE ,
    )
    
"""

FilesReturn="""
    CREATE TABLE FilesReturn(
    FileId INT FOREIGN KEY REFERENCES FILES(ID) ON DELETE CASCADE ,
    Description NVARCHAR(500) 
    )
"""


query1_str=Wlelfare+Category+Estate+State+Role+User+\
           ImageType+Image+Types+Feature+FeatureType+Files+FileImage\
           +FileWlelfare+FilesReturn


DBconect.cursor.execute(query1_str)
DBconect.cursor.commit()
DBconect.closedConection




