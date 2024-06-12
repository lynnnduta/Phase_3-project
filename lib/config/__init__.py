import sqlite3

DATABASE_FILE = 'recipe_manager.db'


CONN = sqlite3.connect(DATABASE_FILE)


CURSOR = CONN.cursor()
