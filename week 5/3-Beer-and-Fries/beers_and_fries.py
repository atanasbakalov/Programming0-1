def max_score(beers, fries):

    rating = 0
    index1 = 0
    index2 = 0


    beers = sorted(beers)
    fries = sorted(fries)

    for index in range (0, len(beers)):
        
        rating += beers[index] * fries[index]
            
    return rating

print(max_score([1000, 1010, 1020, 1030, 1040], [834, 500, -1, 0, 60]))
print(max_score([10, 11], [1, 5]))
print(max_score([5], [5]))



