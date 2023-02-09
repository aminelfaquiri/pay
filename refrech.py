# def my_all(list):
#     for element in list:
#         if bool(element) == False:
#             return False
#     else:
#         return True
#####################################

# def my_any(list):
#     for element in list:
#         if bool(element) == True:
#             return True
#     else:
#         return False
#####################################
# def my_min(MyList):
#     MyList = list(MyList)
#     MyList.sort()
#     return MyList[0]
# #####################################

# def my_max(MyList):
#     MyList = list(MyList)
#     MyList.sort()
#     return MyList[-1]

# #####################################

# friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

# def remove_chars(name):
#     return name[1:-1]

# cleaned_list = map(remove_chars, friends_map)

# for regName in cleaned_list:
#     print(regName)

# for regName in map((lambda name: name[1:-1]), friends_map):
#     print(regName)

# Output
# "Eman"
# "Ahmed"
# "Sameh"
# "Osama"
# #####################################

# friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

# def get_names(n):
#     return n.endswith("m")

# names = filter(get_names, friends_filter)

# for M_name in filter((lambda n: n.endswith("m")), friends_filter):
#     print(M_name)

# # Output
# "Wessam"
# "Essam"

# #####################################
# from functools import reduce
# nums = [2, 4, 6, 2]


# sumAll = reduce(lambda n1, n2: n1*n2, nums)

# print(sumAll)
# print(reduce(lambda n1, n2: n1*n2, nums))

# Output
# 96
# #####################################

# skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")

# for i, el in enumerate(reversed(skills), 50):
#     if type(el) != int:
#         print(f"{i} - {el}")

# import random

# print(random.randrange(10, 50))
# print(random.randrange(2, 10, 2))
# print(random.randrange(1, 9, 2))

# #####################################


# import datetime

# # Print The Current Date and Time
# print(datetime.datetime.now())
# print(datetime.datetime.now().year)
# print(datetime.datetime.now().month)
# print(datetime.datetime.now().day)

# # Print Start and End Of Date
# print(datetime.datetime.min)
# print(datetime.datetime.max)

# # Print The Current Time
# print(datetime.datetime.now().time())
# print(datetime.datetime.now().time().hour)
# print(datetime.datetime.now().time().minute)
# print(datetime.datetime.now().time().second)

# # Print Start and End Of Time
# print(datetime.time.min)
# print(datetime.time.max)

# # Print Specific Date
# print(datetime.datetime(2000, 12, 13))

# #

# myBirthDay = datetime.datetime(2002, 5, 3)
# dateNow = datetime.datetime.now()

# print((dateNow - myBirthDay).days)


#####################################

# import datetime

# print(datetime.datetime.now().strftime("%d"))
