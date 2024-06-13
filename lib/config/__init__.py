import sqlite3

def get_db_connection():
    conn = sqlite3.connect('recipe_manager.db')
    return conn

CONN = get_db_connection()
CURSOR = CONN.cursor()
