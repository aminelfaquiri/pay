# import sqlite module:

import sqlite3

# create data base :
db = sqlite3.connect("rajae.db")

# setting curser :

cr = db.cursor()

# create table and Fields :

cr.execute(
    "CREATE TABLE IF NOT EXISTS Myskills (name text, progress integer, user_id integer)")
cr.execute(
    "CREATE TABLE IF NOT EXISTS User_Client (user_id integer, name text)")

cr.execute("CLEAR TABLE User_Client")
myNAme = ["amin", "hamid", "khalid"]

for k, name in enumerate(myNAme, 1):
    cr.execute(f"INSERT INTO User_Client(user_id, name) VALUES({k},'{name}')")

# cr.execute("INSERT INTO User_Client(user_id, name) VALUES(1,'Rajae')")
# cr.execute("INSERT INTO User_Client(user_id, name) VALUES(2,'Amin')")
# cr.execute("INSERT INTO User_Client(user_id, name) VALUES(3,'Zineb')")
# cr.execute("INSERT INTO User_Client(user_id) VALUES(3)")

db.commit()

cr.close()
