import random
def egg ():
    floors= int(input("enter a number:   "))
    #linear search 
    f = random.randint(1,floors)
    for i in range( 1,floors):
        if i == f:
           print( 'egg is good at floor:' , i)
           print("_"*40)
    # binary search        
    low = 1
    high = floors
    mid = (low+high)//2
    count=0
    for i in range (1, floors,2) :
        if i >= f:        #egg doesnt break
            mid-=1
            count+=1
            print( "egg doesnt break",i)
        else:      # egg break
            mid += 1
            count += 1
            print ("egg breaks at floor",i)
        
    print( count ," <== how many itterations to find the result")
    

egg()          
