def count_elements(items):
    
    counter = 0

    for item in items:
        
        counter += 1
        
    return counter

items = [1, 2, 3, 4, 5, 6, 7]

print("The number of elements in your list is:", count_elements(items))
