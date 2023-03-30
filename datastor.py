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


# Get methods



# Add methods


# Update methods
