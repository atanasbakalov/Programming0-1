def member(x, xs):
    
    found  = False

    for item in xs:
        
        if item == x:
            
            found = True

    return found

print(member(2, [1,2,3,4,5]))

print(member(6, [1,2,3,4,5]))

