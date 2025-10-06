import pyodbc
from config.db import get_connection

try:
    conn = get_connection()
    print("Conexión exitosa a la base de datos gym_db")
    conn.close()
except Exception as e:
    print(f"Error de conexión: {e}")