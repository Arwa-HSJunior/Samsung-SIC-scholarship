### task 1 ###

import random
def guss_within_input_range():
    x = int(input("enter start of the range:\n"))
    y = int(input("enter end of the range:.\n"))


choosed_num = 0
while True:
    for i in range(x, y):
        choosed_num = i  # 3wdna line 83  hna that is what we meant but in the right way
        if i % 5 == 0 and i % 7 == 0:
            print(f"Numbers divisable by 7 & 5 are: {choosed_num}")
    else:
        tryAgain = str(input("play again? (enter Yes or No)")).lower()
        if tryAgain == "yes":
            guss_within_input_range()
        else:
            print("thanks for playing! come back later")
            break


guss_within_input_range()

##### task 2 ####


total_tries = 0
num_list = list(range(1, 101))

user_choice = int(
    input("which number between 1-100 could be the right guess?!"))
for i in num_list:
    i = user_choice
    correct_ans = random.choice(num_list)
    if i < correct_ans:
        total_tries += 1
        print("Lower! ")
        user_choice = int(input("Enter a nmber:\n"))
    elif i > correct_ans:
        total_tries += 1
        print("Higher! ")
        user_choice = int(input("Enter a nmber:\n"))
    elif i == correct_ans:
        total_tries += 1
        print(f"You Won! withtin {total_tries} tries!")
        break
