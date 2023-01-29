# import sqlite module :

import sqlite3

# create Database and conect

db = sqlite3.connect("amin.db")

# create tabel :
db.execute(
    "CREATE TABLE IF NOT EXISTS rajae (name text, progress integer, user_id integer)")

#  close database :

db.close()
