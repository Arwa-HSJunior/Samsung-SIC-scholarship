

# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in  range(2, num)
#         if num % i == 0
#             return False
#     return True

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def is_pronic(num):
    for i in range(num + 1):
        if i * (i + 1) == num:
            return True
    return False



def displayFunc():
    while True:
        print("\nMenu:")
        print("1. check you num if prime\ncheck if num is pronic\nExit")
        choice = input("Enter your choice: ").lower()
    # try:
        num=int(print("enter num to check"))
        if choice == '1' or "prime":
            print(is_prime())
        else:
            print()

def show_menu():
    while True:
        print("1. Say Hello")
        print("2. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            print("hello")
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invslid choice.")

            