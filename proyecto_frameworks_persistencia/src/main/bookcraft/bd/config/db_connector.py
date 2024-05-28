import mysql.connector

class DBConnector:
    def __init__(self):
        self.__connection = mysql.connector.connect(
            host="localhost",
            port="3306", 
            user="root", 
            passwd="root",
            database="biblioteca_db"
        )
    
    def get_connection(self):
        return self.__connection

    def close(self):
        if self.__connection is not None:
            self.__connection.close()