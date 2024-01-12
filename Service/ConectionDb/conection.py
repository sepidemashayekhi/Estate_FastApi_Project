import os
import  pyodbc
from dotenv import load_dotenv


basedir=os.getcwd()
dotenv_path=os.path.join(basedir,'.env')
load_dotenv(dotenv_path=dotenv_path)

ServerName=os.getenv('SERVERNAME')
DbName=os.getenv('DATABASENAME')
Uid=os.getenv('UID')
Password=os.getenv('PASSWORD')



class Conection:
    def __init__(self):

        conn_str = 'DRIVER={ODBC Driver 17 for SQL Server};' \
                   f'SERVER={ServerName};' \
                   f'DATABASE={DbName};' \
                   f'UID={Uid};' \
                   f'PWD={Password}'

        self.cnxn = pyodbc.connect(conn_str)
        self.cursor = self.cnxn.cursor()

    @property
    def closedConection(self):
        self.cnxn.close()