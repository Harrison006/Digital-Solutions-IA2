import os
from unittest import result
from datastore import Datastore

db_file = "dbfile.db"
log = "error_log.txt"

#os.remove(db_file)
#os.remove(log)

db = Datastore(db_file)


db.build_db()

#db.populate_db()
