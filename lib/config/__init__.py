import sqlite3

# Define the path to the SQLite database file
DATABASE_FILE = 'recipe_manager.db'

# Establish a connection to the SQLite database
CONN = sqlite3.connect(DATABASE_FILE)

# Create a cursor object to execute SQL queries
CURSOR = CONN.cursor()
