import  pyodbc

import pyodbc

import pyodbc

class SqlConnection:
    def __init__(self):
        self.cnxnStr = ("Driver={SQL Server};"
                        "Server=DESKTOP-JQNIC8R;"
                        "Database=Estate1;"
                        "Trusted_Connection=yes;")

        self.cnxn = pyodbc.connect(self.cnxnStr)
        self.cursor = self.cnxn.cursor()

    @property
    def closedConection(self):
        self.cnxn.close()