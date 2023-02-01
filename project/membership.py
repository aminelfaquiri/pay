admins = ["Ahmed", "Osama", "Sameh", "Manal", "Rahma", "Mahmoud", "Enas"]

userName = input("Enter Your User Name :").capitalize().strip()


if userName in admins:
    print(f'Hello {userName:s} Welcom Back !')
    yesNo = input(
        "You have edite or change your userName ? y/n").lower().strip()
    if yesNo == "y":
        edit = input("edite or delete ?").lower().strip()
        if edit == "edite":
            newValue = input("Enter Your new Name?").capitalize().strip()
            admins[admins.index(userName)] = newValue
        elif edit == "delete":
            admins.remove(userName)
        else:
            print("Somting Woring !")
    else:
        print(f"Welcom {userName:s} !")
else:
    print("Not Found User !")
    yesNo = input("Register Now ? y/n ").lower().strip()
    if yesNo == "y":
        print("Regestrating succesfule !")
        admins.append(userName)
    else:
        print(f"thank you {userName:s} for intrested !")
print("#"*80)
print(admins)
print("#"*80)
