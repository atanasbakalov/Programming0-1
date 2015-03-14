n = int(input("Въведете долна граница N:" + "\n"))
m = int(input("Въведете горна граница M:" + "\n"))

start = n

while n <= m:

    start = n

    sum_digits = 0

    while start != 0:

        digit = start % 10

        sum_digits += digit

        start = start // 10

    print (n, "- sum of digits is:", sum_digits)

    n += 1


    
  


