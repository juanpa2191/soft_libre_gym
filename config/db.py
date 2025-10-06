import pyodbc

def get_connection():
    return pyodbc.connect(
        "Driver={MySQL ODBC 9.4 Unicode Driver};"
        "Server=localhost;"
        "Database=gym_db;"
        "PORT=3306;"
        "user=root;"
        "password=I6p4maez."
    )