import sqlite3


db = sqlite3.connect("amin.db")

cr = db.cursor()

cr.execute(
    "CREATE TABLE IF NOT EXISTS 'MyLove'(name text, age integer, prog integer)")

# cr.execute("INSERT INTO MyLove(name,age,prog) VALUES('zineb',20,80) ")

# cr.execute("SELECT COUNT(*) FROM MyLove")
cr.execute("SELECT name FROM MyLove ORDER BY name ")
# cr.execute("SELECT name FROM MyLove")

print(cr.fetchall())

db.commit()

db.close()
