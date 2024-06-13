import sqlite3

CONN = sqlite3.connect('db/recipe_manager.db')
CURSOR = CONN.cursor()

def close_connection():
    CONN.close()

def initialize_database():
    
    pass
