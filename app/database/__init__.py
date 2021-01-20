
import sqlite3

def connect(factory=None):
    
    connection = sqlite3.connect('database/database.db')
    
    if factory:
        connection.row_factory = factory
    
    return connection


def setup():

    with open('database/setup.sql') as file:
        
        cursor = connect().executescript(file.read())
        cursor.connection.commit()
        cursor.close()
