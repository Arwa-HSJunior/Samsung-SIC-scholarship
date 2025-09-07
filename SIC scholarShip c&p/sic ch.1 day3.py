# # exersice 1
# # x = int(input("Enter 1st number please: "))
# # y = int(input("Enter 2st number please: "))
# # print(x+y)

# # ### exersice 2
# # x = int(input("Enter a number: "))
# # if x%2 == 0:
# #     print("number is even")
# # elif x%2 != 0:
# #     print("number is odd")

# # exersice 3
# # field try needs answers!
# # while True:
# #     try :
# #         x= int(input("Enter X: \n"))
# #         print(f"1st number is:{x}")
# #         break
# #     except ValueError:
# #         print(x)
# # while True:
# #     try:
# #         y = int(input("Enter Y: \n"))
# #        print("1st number is:\n")
# #     except ValueError:
# #         print("That is not a valid integer. please try again")
# ####

# # def add(a, b):
# #    return a+b
# # a = int(input("please enter x:\n"))
# # b = int(input("please enter y:\n"))

# # print("choose operations\n 1.add\n 2.subtract\n 3.multiply\n 4.division")
# # choosed_operation = int(input("Choose an operation by entering: (1, 2, 3, 4)\n"))
# # if choosed_operation == 1 :
# #     result = add(a, b)
# # elif choosed_operation == 2:
# #     result = subtract(a, b)
# # elif choosed_operation == 3:
# #     result = multibly(a, b)
# # elif choosed_operation == 4 :
# #     result = division(a, b)
# # else:
# #     result="invalid operation"
# def calculator():
#     while True:
#         def add(a, b): return a+b
#         def subtract(a, b): return a-b
#         def multibly(a, b): return a*b
#         def power(a, b): return a**b

#         def safeDivide(a, b):
#             try:
#                 return a/b
#             except ZeroDivisionError:
#                 return "error: cannot divide by zero"
#             except ValueError:
#                 return "error: enter valid numbers "

#         def division(a, b): return safeDivide(a, b)

#         try:
#             a = int(input("Please enter x:\n"))
#             b = int(input("Please enter y:\n"))
#             choosed_operation = int(input("Choose an operation by entering: (1, 2, 3, 4, 5)\n1. Add\n2. Subtract\n3. Multiply\n4. Division\n5. power\nSelect: "))

#             if choosed_operation == 1:
#                 result = add(a, b)
#             elif choosed_operation == 2:
#                 result = subtract(a, b)
#             elif choosed_operation == 3:
#                 result = multibly(a, b)
#             elif choosed_operation == 4:
#                 result = division(a, b)
#             elif choosed_operation == 5:
#                 result = power(a, b)
#             else:
#                 result = "Invalid operation"
#             print(f"Result = {result}")

#         except ValueError:
#             print("Error: Please enter valid numbers")
#         break

# while True:
#     calculator()
#     ask_again = input("Do you want to perform another calculation? (yes/no): ").lower()
#     if ask_again != 'yes':
#         break

# # exercise 4
# # guess random dice number

# # import random
# # gussing_dice_number = int(input("guess a number from 1-6 \n"))
# # while True:
# #     i = random.choice(range(6))
# #     if  gussing_dice_number == i:
# #     # for i in range(1,6):
# #         print(f"You gussed the right number {gussing_dice_number}")
# #         break
# #     else:
# #         gussing_dice_number = int(input("bad luck, try again! guess a number from 1-6 \n"))


# # exercise 5 fabionaccie series
# #    not solved


# ### task 1 ###

# # i modified this previous given task with recursion

# # def guss_within_input_range() :
# #     x = int(input("enter start of the range:\n"))
# #     y = int(input("enter end of the range:.\n"))
# # # choose_within_range = int(input("choose a number within x&y (both included)"))
# #     choosed_num = 0
# #     while True:
# #         for i in range(x, y+1): # y+1 3shan tb2a included w el X kda kda m3ana
# #             choosed_num = i #3wdna line 83  hna that is what we meant but in the right way
# #             if i % 5 == 0 and i % 7 == 0:
# #                 print(f"Numbers divisable by 7 & 5 are: {choosed_num}")
# #         else:
# #             tryAgain = str(input("play again? (enter Yes or No) 56")).lower()
# #             if tryAgain == "yes":
# #                 guss_within_input_range() # <== here is recursion
# #             else:
# #                 print("thanks for playing! come back later")
# #                 break
# # guss_within_input_range()


# ##### task 2 ####
# # import random


# # total_tries = 0
# # num_list = list(range(1, 101))

# # user_choice = int(input("which number between 1-100 could be the right guess?!"))
# # for i in num_list:
# #     i = user_choice
# #     correct_ans = random.choice(num_list)
# #     if i < correct_ans:
# #         total_tries += 1
# #         print("Lower! ")
# #         user_choice = int(input("Enter a nmber:\n"))
# #     elif i > correct_ans:
# #         total_tries += 1
# #         print("Higher! ")
# #         user_choice = int(input("Enter a nmber:\n"))
# #     elif i == correct_ans:
# #         total_tries += 1
# #         print(f"You Won! withtin {total_tries} tries!")
# #         break


####  Mini Project: Student Info & Score Analyzer ####
name = input("please enter your name: ")

age = int(input("Please enter you age: "))

if age < 18:
    print("You are too young!")
else:
    print("Welcome to the system")
    print(f"Welcome Student {name}".upper())


def average(deg1, deg2, deg3):
    global averg
    averg = 0
    for i in range(3):
        averg = (deg1 + deg2 + deg3)/3

    print("Average score =", averg)
    if averg >= 50:
        print("Result: Passed")
    else:
        print("result = Failed")


score1 = int(input("Enter score 1:"))
score2 = int(input("Enter score 2:"))
score3 = int(input("Enter score 3:"))
print("scores: ")
print(score1)
print(score2)
print(score3)
average(score1, score2, score3)

print("First 3 letters of your name: ", name[0:3])

message = "i love python"
print(message)
print("after.replace: ", message.replace("python", "mama"))
message = "i love python"
print("After split: ", message.split())

print("Global variable test: ", averg)
