
import sqlite3
db = sqlite3.connect("Rajae.db")
cr = db.cursor()
cr.execute(
    "CREATE TABLE IF NOT EXISTS MySkills(skil text, prograsse integer, userId integer)")

userId = 2

inpute_Message = """ What Do You Want To Do ?
"s" = > Show All Skills
"a" = > Add New Skill
"d" = > Delete A Skill
"u" = > Update Skill Progress
"q" = > Quit The App
Choose Option:
"""

inpute_Message = input(inpute_Message.strip().lower())

commands_list = ["s", "a", "d", "u", "q"]

# set function :


def show_data():
    cr.execute("SELECT skil, prograsse FROM MySkills")
    result = cr.fetchall()
    print(f"All Your Skills Is {len(result)} :")
    for s, p in result:
        print(f"Skil :{s},Prograsse => {p}")

    close_connection()


def add_data():

    skil = input("Plese Enter Your Skills :").strip().capitalize()
    prog = input(f"Plese Enter Your Prograss Of {skil} :")

    cr.execute(f"SELECT skil FROM MySkills WHERE skil='{skil}'")

    if cr.fetchone() == None:
        cr.execute(
            f"INSERT INTO MySkills(skil,prograsse,userId) VALUES('{skil}',{prog},{userId})")
        print("Adeed")
    else:
        print("this Skills Alredy Exists")
        desision = input(
            "You want to update your data : y/n ? ").strip().lower()
        if desision == "y":
            print("Please Enter Yor old_Skill And New_Skill :")
            old = skil
            new = input("Please Enter New Skil :").strip().capitalize()
            prog = prog

            cr.execute(
                f"UPDATE MySkills SET skil = '{new}' WHERE skil = '{old}' ")
            cr.execute(
                f"UPDATE MySkills SET prograsse = '{prog}' WHERE skil = '{new}' ")

            print("Value Is Update !")
        else:
            print("Thank You !")
    # ----------------------------------------------
    # cr.execute("SELECT skil FROM MySkills")

    # result = []
    # for sk in cr.fetchall():
    #     result.append(sk[0])

    # if skil not in result:
    #     cr.execute(
    #         f"INSERT INTO MySkills(skil,prograsse,userId) VALUES('{skil}',{prog},{userId})")
    #     print("Adeed")
    # else:
    #     print("this Skills Alredy Exists")
    # ----------------------------------------------
    close_connection()


def delete_data():
    dlt_Value = str(input("Please Enter Your Delete :").strip().capitalize())
    cr.execute(
        f"DELETE FROM MySkills WHERE skil='{dlt_Value}' AND userId={userId}")
    print("Delete Success !")
    close_connection()


def update_data():

    print("Please Enter Yor old_Skill And New_Skill :")
    old = input("Please Enter Old Skil :").strip().capitalize()
    new = input("Please Enter New Skil :").strip().capitalize()
    prog = input("Please Enter Your Prograsse :")

    cr.execute(f"UPDATE MySkills SET skil = '{new}' WHERE skil = '{old}' ")
    cr.execute(
        f"UPDATE MySkills SET prograsse = '{prog}' WHERE skil = '{new}' ")

    print("Value Is Update !")
    close_connection()


def close_connection():
    db.commit()
    db.close()


# Check command :
if inpute_Message in commands_list:

    if inpute_Message == "s":
        show_data()

    elif inpute_Message == "a":
        add_data()

    elif inpute_Message == "d":
        delete_data()

    elif inpute_Message == "u":
        update_data()

    else:
        db.commit()
        db.close()

else:

    print(f"Sorry This Command {inpute_Message} is Not Found!")
