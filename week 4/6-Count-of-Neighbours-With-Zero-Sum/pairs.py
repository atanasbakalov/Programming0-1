def count_zero_neighbours(numbers):
    
    count = 0
    index = 0

    for number in numbers:
        
        if index < len(numbers) - 1:
            
            neighbour = numbers[index + 1]

            if number + neighbour == 0:
                
                count += 1
                
        index += 1

    return count

print("There are", count_zero_neighbours([1, 2, 3, -1, -2, -3]),
      "zero neighbours in this list.")

print("There are", count_zero_neighbours([1, 2, 3, 4, 5]),
      "zero neighbours in this list.")
