a = int(input("Type lower bound" + "\n"))
b = int(input("Type upper bound" + "\n"))
x = int(input("Type x:" + "\n"))

if x == a:
    
    print ("The number is equal to the lower bound of the interval")
    
elif x == b:
    
    print ("The number is equal to the upper bound of the interval")
    
elif x > a and x < b:
    
    print ("The number is in the interval")
    
elif x < a:
    
    print ("The number is outside the interval, x < a")
    
elif x > b:
    
    print ("The number is outside the interval, x > b")




