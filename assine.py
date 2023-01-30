
userNAme = input("Please Enter Your Name ?").strip().capitalize()
age = int(input("Please Enter Your Age ?"))
print("#" * 100)
print(" You can Write Time Unite as Second , Month , Days, Years Or first letter (s,m,d,y) ".center(100, "#"))
print("#" * 100)
ageUnite = input("Please Enter Your Age Unite ?").strip().capitalize()

ageMonth = age * 12
ageWeek = ageMonth * 4
ageDays = age * 365
ageHours = ageDays * 24
ageMinute = ageHours * 60
ageSeconds = ageMinute * 60

print(f"Hello Dear {userNAme:s} !")

if ageUnite == "Month":
    print(f'Your Age Is {ageMonth:,} Months')
elif ageUnite == "Week":
    print(f'Your Age Is {ageWeek:,} Weeks')
elif ageUnite == "Day":
    print(f'Your Age Is {ageDays:,} Days')
elif ageUnite == "Hour":
    print(f'Your Age Is {ageHours:,} Hours')
elif ageUnite == "Minute":
    print(f'Your Age Is {ageMinute:,} Minutes')
elif ageUnite == "Second" or 's':
    print(f'Your Age Is {ageSeconds:,} Seconds')
else:
    print(f'Your Age Is {age} years')
