import pyodbc

conn_str = (
    r"Driver={SQL Server Native Client 11.0};"
    r"Server=(localdb)\MSSQLLocalDB;"
    r"Database=C:\USERS\JOHN-\ONEDRIVE\DOKUMENT\SQL ASSIGNMENT.mdf;"
    r"Trusted_Connection=yes;"
)

connection = pyodbc.connect(conn_str)

cursor = connection.cursor()
