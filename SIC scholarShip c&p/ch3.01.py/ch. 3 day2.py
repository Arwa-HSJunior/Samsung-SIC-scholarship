#### factorial logic is cracked in my brain fix it ofc####


#### second exersise ####
while True:
     try:
          userL = input("enter your list by space between each number: ")
          user_list = list(map(int,userL.split()))
          print("list =", user_list)
          x=int(input("enter a number willl be  x2 and used to identify index\n"))
          x = x*2
          # x*=2
          print("this is the indexed value",user_list[x])
     except IndexError:
          print("index is out of list range ")
     except ValueError: 
          print("please enter a valid number ")
     else:
          print("thank youuu ")
     finally:
          print("you can try again if you want !")
