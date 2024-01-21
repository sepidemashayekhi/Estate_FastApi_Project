import os
import  pyodbc
from dotenv import load_dotenv


SERVERNAME='localhost,1533'
DATABASENAME='ESTATE'
UID='SA'
PASSWORD='MyStrong@Passw0rd'



class Conection:
    def __init__(self):

        conn_str = 'DRIVER={ODBC Driver 17 for SQL Server};' \
                   f'SERVER={SERVERNAME};' \
                   f'DATABASE={DATABASENAME};' \
                   f'UID={UID};' \
                   f'PWD={PASSWORD}'

        self.cnxn = pyodbc.connect(conn_str)
        self.cursor = self.cnxn.cursor()

    @property
    def closedConection(self):
        self.cnxn.close()