import pyodbc

conn_str = (
    r"Driver={SQL Server Native Client 11.0};"
    r"Server=(localdb)\MSSQLLocalDB;"
    r"Database=C:\USERS\JOHN-\ONEDRIVE\DOKUMENT\SQL ASSIGNMENT.mdf;"
    r"Trusted_Connection=yes;"
)

connection = pyodbc.connect(conn_str)

cursor = connection.cursor()

cursor.execute("select top 3 country from countries")
row = cursor.fetchall()
if row:
    print(row)

cursor.execute("select top 3 * from SoccerResults")
row = cursor.fetchall()
if row:
    print(row)
