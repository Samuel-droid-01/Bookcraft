import mysql.connector

class DBConnector:
    def __init__(self):
        self.__connection = mysql.connector.connect(
            host="localhost",
            user="root", 
            password="utm2024",
            database="bibilioteca_db"
        )
    
    def get_connection(self):
        return self.__connection

    def close(self):
        if self.__connection is not None:
            self.__connection.close()