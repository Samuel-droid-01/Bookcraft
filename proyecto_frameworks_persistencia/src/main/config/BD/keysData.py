import mysql.connector

class Database:
    def __init__(self):
        self.conexion = None

    def connect(self):
        self.conexion = mysql.connector.connect(
            host="localhost", 
            user="root", 
            passwd="utm2024",
            database="bibilioteca_db"
        )
        return self.conexion.cursor()

    def disconnect(self):
        if self.conexion is not None:
            self.conexion.close()