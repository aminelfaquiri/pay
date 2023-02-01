#
# site = []

# maxSite = 5

# while maxSite > 0:
#     print("#" * 80)
#     print(f" You have {maxSite if maxSite != 1 else 'The Last'} Position avalibel ".center(
#         80, "#"))
#     print("#" * 80)
#     siteInpute = input("Please Enter Your Site withoute \"https://www.?\"")
#     site.append(f'https://www.{siteInpute}')
#     maxSite -= 1
#     print(site)
# else:
#     print("Your boobmark is full")

# mainPass = "aminrajae"

# tria = 4

# passInpute = input("Please Enter Your Pass :")

# while passInpute != mainPass:

#     tria -= 1

#     print(f"Pass Woring You have [{'Last' if tria == 1 else tria }] Chance !")

#     passInpute = input("Please Enter Your Pass :")

#     # final woring :
#     if tria == 1:
#         print("Sorry !")
#         break

# else:
#     print(f"Welcom Dear {passInpute}!")

# while tria > 0:
#     passInpute = input("Please Enter Your Pass :")
#     tria -= 1
#     if passInpute == mainPass:
#         print("Welcom Back Dear!")
#         break
#     elif tria != 0:
#         print(f"Pass Woring [{tria}] Try left !")
#     else:
#         print("Sorry We think You are hacker !")

#  Loop :

# for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:

#     if i % 2 != 0:
#         print(f'odd Number => {i}')
#     else:
#         print(f'Even Number => {i}')

# peoples = ["Osama", "Ahmed", "Sayed", "Ali"]

# skills = ['Html', 'Css', 'Js']

# for i in peoples:
#     print(f"{i} :")
#     for s in skills:
#         print(f'- {s}')
# else:
#     print("Fineshed!")


# peoples = {
#     "Osama": {
#         "Html": "70%",
#         "Css": "80%",
#         "Js": "70%"
#     },
#     "Ahmed": {
#         "Html": "90%",
#         "Css": "80%",
#         "Js": "90%"
#     },
#     "Sayed": {
#         "Html": "70%",
#         "Css": "60%",
#         "Js": "90%"
#     }
# }


# for i in peoples:
#     print(f"The skils Of '' {i.upper()} '' Is :")
#     for skils in peoples[i]:
#         print(f'- {skils.upper()} => {peoples[i][skils]}')


# for i in range(0, 10):
#     if i == 3:
#         pass

#     print(i)

# myUltimateSkills = {
#     "HTML": {
#         "Main": "80%",
#         "Pugjs": "80%"
#     },
#     "CSS": {
#         "Main": "90%",
#         "Sass": "70%"
#     }
# }

# for k, v in myUltimateSkills.items():

#     print(f'{k} :')
#     for kk, vv in v.items():
#         print(f"- {kk.lower()} => {vv}")


def sayHello():
    return "hello Amin"


x = sayHello()

print(x)
