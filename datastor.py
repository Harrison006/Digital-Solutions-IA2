import random
import sqlite3
from unittest import result

class Datastore():
    def __init__(self):
        """
        INitilaise the data stre by connecting to the sqlite db
        """
        db_file = "RTR_db.db"
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()
    def __del__(self):
        self.connection.close()
    
    def build_db(self):

        self.cursor.execute(
                """
                CREATE TABLE patient(
                    name TEXT NOT NULL)
                """
# Get methods



# Add methods


# Update methods
