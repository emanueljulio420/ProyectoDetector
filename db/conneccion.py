import sqlite3
from sqlite3 import Error

def create_connect():

    try:
        conn = sqlite3.connect('db/user.db')
        return conn
    except Error as e:
        print('Error al conectoar con la base de daots '+ str(e))
        