# btl1 =100
# btl2 =200
# btl3 =400
# print(btl1 + btl2 + btl3 / 3)

# l_1= [1,2,3,4]
# l_2=[1,2,3,4]
# sum=[]
# for i in range(0,len(l_1)):
#     sum.append(l_1[i]+l_2[i])

# print(sum)

# #### remove duplicate ####
# input1= input("enter a spaced nums list to remove duplicates: ")
# real_input= list(map(int,input1.split()))
# print("your list: ",real_input)
# cleanList=[]
# for i in real_input:
#     if i not in cleanList:
#         cleanList.append(i)
# print(tuple(cleanList))


###### person's height ####

# names = input("enter a spaced names list: ")
# name = list(map(str, names.split()))
# print("your list: ", name)

# height= input("enter a spaced persons heights list: ")
# heigh = list(map(int, height.split()))
# print("your list: ",heigh)
# names =[]
# for i in name:
#     names.append(i)
# heights=[]
# for i in height:
#     heights.append(i)
# print(names )
# print(heights)

# heightFromName = {"ahmed": 165, "mohamed": 178, "mahmoud": 195}
# nameToFind = input("Please enter the name of the participant: ")
# result = heightFromName.get(nameToFind, "Name not found, please try again.")
# print(result)

# names = input("enter a spaced names list: ")
# name = list(map(str, names.split()))
# outL=[]
# for i in range(len(name)):
#     pname = len(name)
#     if i < pname:
#         outL.append(i)

# print("your list: ", outL)
# nameL=[]
# input_= list(input("enter 5 names").split())

# names = input("Enter 5 words separated by spaces:  ").split()
# while len(names) !=5:
#     print("Please enter exactly 5 words.")
#     words = input("Enter 5 words separated by spaces: ").split()

# min_length = len(names[0])
# for name in names:
#     if len(name) < min_length:
#         min_length=len(names)

# shortest_words=[]
# for shortest in names:
#     if len(shortest) == min_length:
#         shortest_words.append(shortest)

# print("shortes names: ", shortest_words)


Example_list = [4, 9, 1, 1, 2, 2, 4, 3, 2, 1, 6, 4, 1, 4, 3, 4, 2, 2, 9, 9, 3, 2, 6, 1]
sortedlist = sorted(Example_list)
print("sortedlist: ", sortedlist)
no_dou = []
for i in Example_list:
    if i not in no_dou:
        no_dou.append(i)
print(no_dou)


# for i in range(len(sortedlist) - 1):
#     if sortedlist[i] != sortedlist[i + 1]:
#         no_dou.append(sortedlist[i])

# # لازم نضيف آخر عنصر لأنه مش هيتقارن مع اللي بعده
# no_dou.append(sortedlist[-1])

# print("With no duplicates: ",no_dou)

# Write down the computational results for the following two sets.
# s1 = {10, 20, 30, 40}
# s2 = {30, 40, 50, 60, 70}

# Find the results from 1) to 7).
# print(s1 |s2)
# print(s1 & s2)
# print(s1 - s2)
# print(s1 ^ s2)
# print(s1.issubset(s2))
# print(s1.issuperset(s2))
# print(s1.isdisjoint(s2))

#______________________________
# Create a list of 10 numbers.
# Find the max, min, sum, and average.
# Then convert it into a tuple.

# creat a list
#we look for the biggest number by a conditon in a loop
#we print this biggest number in a list
#then we print this list as tuple()

#for min number for the same list
#itterate about our list 
# we look for the smallest number by using a condition
# then store this output in a list
# and then print this list as a tuple()

#creat a list
#access each nmber in the list like using loops
#make summtion for each number in each itteraation
#incrment another variable by the value of this number
#we define the incremented variable before loop asignning it to zero
#then we acuatly print the incremented variable in the avreage result 


#main dict for student info
#assigns key of name and age to the user values idk how they are inputed
# then make another dict inside main one have his grades info
# and if the condtion fullfiled for the avrg grabd done by a function asign it to True
# otherwise if not fullfilled then False
#in both you print the result if passed = to ture or false
#then play with the keys and values of any dict using built in functions
# use built in functions that itterate on each key or value in the dict
#use other ones that adds ar remove gennerally


#IMPORT A jason file
# then use bult in function like read and print a string sayin we are reading file
# then displaying the data from json in a dictionary


# make a lists of all types and a dictionary 
# make a condition that is a chekker to fnd a ceartin item in all lists or dict
# check this in each item in separate lines of code
# and print them also in a different lines of code

# Matrix:
# [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]

# Diagonal Elements: 1 5 9
# approach the matrix syntax 
# know how o right the diagonal type of matrxies
#and know how to acces the diagonal elements 
#know if they are accesd individually or as whole 
#know if you alsan need to acces them by a method or it is done when we write the matrix form the first place
# by storing them in a variable the is = any matrix propably
#then use how you acces them in the print statment o be output in a one line 