import mysql.connector
def db_connection():
    conexion1=mysql.connector.connect(
        host="localhost", 
        user="root", 
        passwd="utm2024",
        database=" 	bibilioteca_db"
        
        
        )
    conexion=conexion1.cursor()
    return conexion

