# x = int(input("please enter X: "))
# y= int(input("please enter Y: "))

# # choice= int(input("Please choose operation (1, 2, 3, 4, 5)"))
# # if choice== 1:
# #     print(x + y)
# # elif choice==2:
# #     print(x-y)
# # elif choice==3:
# #     print(x*y)
# # elif choice==4:
# #     print(x^y)
# # elif choice == 5:
# #     print(x/y)

# def add(x,y):
#     return x+y

# add(x,y)


# تدريب على الركرشن
# def countdown(n):
#     if n ==0 :
#         return
#     if n == 51 :
#         return
#     elif n %5==0:
#         print("BOOM!")
#     else:
#         print(n)
#     countdown(n+1)

# countdown(1)

import json


class scholarshipsAwards:
    def __init__(self, name, title, description):
        self.title = title
        self.description = description
        self.name = name

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"Identity: {self.title}\n"
            f"Discription: {self.description}\n\n"
        )

    def __repr__(self):
        return self.__str__()


scholar = scholarshipsAwards(
    "arwa\n\n", "lovely funny student", "description NOne لان الوصف لله وحدة")
print(scholar)


# mini project craeat data in separate json file and load it in another file i.e. here!"
with open("ch3.01.py/JSON.1st.json", "r") as file:
    loaded_data = json.load(file)
print(loaded_data["name"], "is a student in ", loaded_data["scholarships"])

### de el main menu ###
nums = []

while True:
    print("MAIN MENU ", " ")
    print("1. Add number")
    print("2. Show numbers")
    print("3. Delete numbers")
    print("0. Exit")
    choice = input("Enter your Choice: ")
    if choice == '1':
        number = int(input("Add a Number: "))
        nums.append(number)
    if choice == '2':
        print("List= ", nums)
    if choice == '3':
        nums.pop()
        print(nums)
    if choice == '0':
        break
