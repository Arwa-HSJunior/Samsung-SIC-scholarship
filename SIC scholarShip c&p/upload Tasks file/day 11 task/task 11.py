import random


def searching_Methods():
    n = int(input("enter a number of floors:   "))
    low = 1
    high = n
    count = 0
    f = random.randint(1, n)

    print("\nLinear Search:")  # 3enwan
    for i in range(1, n):
        count += 1   # how many times it itirates
        if i == f:
            print("Finally the safe floor for dear egg : ", i)
            print("Steps count = ", count)
    
    print("_"*25)

    print("\nBinary Search:")  # 3enwan
    while high >= low:  # minfa3sh high a2l mn low , equal low tesmhy 3ady
        count += 1    
        mid = (low+high)//2
        if f > mid:
            low = mid + 1
        elif f < mid:
            high = mid - 1
        else:
            print("Finally the safe floor for dear egg : ", mid)
            print("Steps Count = ", count)
            break


searching_Methods()


def search_methods():
    floors =int(input("please enter number of loors"))
    f = random.randint(1, floors)
    low = 1
    upper = f
    count =0
    while upper>= low:
        count +=1
        mid = (upper+low)//2
        if f < mid:
            upper = mid-1
        if f > mid:
            low = mid +1
        else:
            print("Finally the safe floor for dear egg : ", mid)
            print("Steps Count = ", count)
            break


search_methods()































