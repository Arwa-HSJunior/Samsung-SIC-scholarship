# chapter 1 unit 3

###exercise###
# print("arwa", "ashraf", "muhammed", sep="-")
# print("arwa", end="-")
# print("ashraf ", end="-")
# print("mohammed ",)

# arwa = ["muslim", "girl", "in egypt"]
# output = "-".join(arwa)
# print(output)

# x = input("enter 1st num:")
# y = input("enter 2nd num: ")
# print(x+y)

# exercise 4 in slides

### making sure user enters a nymber for age or try again message pops
## a try for exception handeling need itterations
# def input_age():
#     if age == int(input("Enter your age: ")):
#         return age
#     else:
#         print("Enter your age: ")


# user_infos = {
#     "name": str(input("Enter your name: ")),
#     "age":  int(input("Enter your age: ")),
#     "uni":  str(input("Enter you university: ")),
# }

# print(user_infos)

### Task 1 ####

fav_color= str(input("Enter your favourtie color: "))
fav_food = str(input("Enter your favourite food: "))
city = str(input("Enter City of residense: ")).title()

print(f"Your favourite color is {fav_color}, you love eating {fav_food} and you live in {city}")