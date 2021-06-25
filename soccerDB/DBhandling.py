import pyodbc


class Database:
    def __init__(self):
        self.conn_str = (
            r"Driver={SQL Server Native Client 11.0};"
            r"Server=(localdb)\MSSQLLocalDB;"
            r"Database=C:\USERS\JOHN-\ONEDRIVE\DOKUMENT\SQL ASSIGNMENT.mdf;"
            r"Trusted_Connection=yes;"
        )
        self.connection = pyodbc.connect(self.conn_str)
        self.cursor = self.connection.cursor()

    def fetchCountries(self):
        self.cursor.execute("SELECT UNIQUE [Home Team] FROM SoccerResults")
        return self.cursor.fetchall()
