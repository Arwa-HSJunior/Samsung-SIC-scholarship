# x = int(input("enter x:\n"))
# y = int(input("enter x:\n"))

##### exercise 1####
# def shebsy(x, y):
#     return (x+y)*(y-x)

# print(f"number for shebsy" {shebsy(x, y)}")
# print ("number for shebsy Methodology",shebsy(x, y) )
# r=0

##### exercise two #####
# def add(x, y):
#     return x+y


# x = int(input("enter x:\n"))
# y = int(input("enter x:\n"))
# print(add(x, y))

# EX 4


# def add(**kwargs):
#     return x+y


# while True:
#     user_input = int(input("enter a numbers:\n"))     #craked code needs try ex.4 again
#     numbers = [int(i) for i in user_input.split()]
#     print(add(numbers))

#     break


# tmep_celsius = list[25,30,35,40]
# temp_fahrenheit = lambda fahrn:(tmep_celsius*9/5)+32
# result = list(map (temp_fahrenheit, tmep_celsius))
# print(result)


# shebsy again#

# def shebsy(x ,y):
#     return (x+y)*(y-x)

# x= int(input("enter x: "))
# y = int(input("enter y: "))
# print("the shebsy number for 7 and 12: ",shebsy(x, y))

# def add(x+y):
#     return x+y

# x = int(input("enter x: "))
# y = int(input("enter y: "))
# print(add(x,y))


# def add(*nums):
#     summition_user_values=0
#     for i in range(len(nums)):  # عشان عايزا اعرف العدد الي دخلة في نامز مش اللي جوا نامز
#         summition_user_values += nums[i]
#     return summition_user_values

# print(add(1, 2, 3, 4, 5, 6, 7))


# name= ["arwa","ashraf","mohammed"]

# def douple(alist):
#     return alist *2

# doupleName = map(douple,name)

# doupleNametupels = list(doupleName)
# print(doupleNametupels)

# celecius = [26, 25 , 100]
# fahren=map(lambda deg : (deg*9/5)+32, celecius)
# # fahrenDeg=tuple(fahren)
# # print((fahrenDeg))
# print(list(fahren))

# Imagine the problem were more complex, convert from F to C and vice versa, and the input is taken from the user

def TempConv():
    OutputList = []

    # Step 1: دخل درجات الحرارة
    temp_input = input("Enter temperatures separated by spaces:\n")
    listOfTemps = list(map(float, temp_input.split()))

    # Step 2: اسألي المستخدم عايز يحول إيه
    while True:
        choice = input("Enter 1 to convert from Celsius to Fahrenheit, or 2 for Fahrenheit to Celsius:\n")
        if choice in ["1", "2"]:
            break
        print("Invalid choice. Please enter 1 or 2.")

    # Step 3: التحويل بناءً على الاختيار
    if choice == "1":
        for i in listOfTemps:
            OutputList.append((i * 9/5) + 32)
    elif choice == "2":
        for i in listOfTemps:
            OutputList.append(5/9 * (i - 32))

    # Step 4: عرض النتيجة
    print("Converted temperatures:", OutputList)

TempConv()