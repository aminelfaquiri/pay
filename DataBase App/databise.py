
import sqlite3
db = sqlite3.connect("Rajae.db")
cr = db.cursor()


def ShowAllSkilss():
    cr.execute("SELECT * FROM skills")

    allskills = []

    for i in cr.fetchall():
        allskills.append(i[0])

    return allskills


inpute_Message = """ What Do You Want To Do ?
"s" = > Show All Skills
"a" = > Add New Skill
"d" = > Delete A Skill
"u" = > Update Skill Progress
"q" = > Quit The App
Choose Option:
"""
inpute_Message = str(input(inpute_Message.strip().lower()))

# Show Skills :
if inpute_Message == "s":
    cr.execute("SELECT * FROM skills")
    result = cr.fetchall()
    print("Your Skills Is :")
    for k, v in result:
        print(f"{k} => {v}%")

# add new skills :
elif inpute_Message == "a":
    skl = str(input("Enter Skils Please skil  :"))
    prog = str(input(f"Enter Progress Of {skl} Please :"))
    cr.execute(f"INSERT INTO skills(skil,prograsse) VALUES('{skl}',{prog})")
    print("Your Skill Is Added !")

# delete :
elif inpute_Message == "d":

    print(ShowAllSkilss())
    delName = input("Please Enter Your Delete Skil :")
    cr.execute(f"DELETE FROM skills WHERE skil = '{delName}'")
    print("delete success !")

#  Update :
elif inpute_Message == "u":

    print(ShowAllSkilss())

    oldValue = input("Please Enter Your Old Value :")
    newValue = input("Please Enter Your Old Value :")

    cr.execute(
        f"UPDATE skills SET skil = '{newValue}' WHERE skil = '{oldValue}'")

    print("Your Data Is Updated !")

elif inpute_Message == "q":
    print("App Quite !, Have A Good Day !")

else:
    print("Messing Entreis ('_')")


cr.execute("SELECT * FROM skills")
print("Finally Skills List :")
print(cr.fetchall())
db.commit()
db.close()
