def count_zero_pairs(numbers):
    
    count = 0
    
    n = len(numbers)
    
    for i in range(0, n):
        
        for j in range(i, n):
            
            x = numbers[i]
            y = numbers[j]

            if x + y == 0:
                
                count += 1

    return count

print(count_zero_pairs([1, 2, 3, -1]))
print(count_zero_pairs([1, 2, 3, 4, 5]))
print(count_zero_pairs([0, 2, -2, 5, 10]))

