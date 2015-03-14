n = int(input("Type a number of perfects to show:" + "\n"))

number = 1

perfect_numbers = []

count_perfects = 0

while number <= 137438691328:
        
    sum_factors = 0
        
    for i in range(1, number):
            
        if number % i == 0:
                
            sum_factors += i
                
    if sum_factors == number:

        perfect_numbers = perfect_numbers + [number]

        count_perfects += 1

    if count_perfects == n:

        break

    number += 1

print("The first", n, "perfect numbers are", perfect_numbers)

    

    

        
        
        

       



