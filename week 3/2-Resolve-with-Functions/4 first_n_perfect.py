def first_n_perfect(n):

    number = 1

    perfect_numbers = []

    count_perfects = 0

    while number <= 137438691328:
        
        sum_divisors = 0
        
        for i in range(1, number):
            
            if number % i == 0:
                
                sum_divisors += i
                
        if sum_divisors == number:

            perfect_numbers = perfect_numbers + [number]

            count_perfects += 1

        if count_perfects == n:

            break

        number += 1

    return perfect_numbers

n = int(input("Type a number of perfects to show:" + "\n"))

print(first_n_perfect(n))
