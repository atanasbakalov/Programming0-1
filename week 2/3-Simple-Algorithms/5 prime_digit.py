n = int(input("Type a number" + "\n"))

while n != 0:

    digit = n % 10

    start = 2

    is_prime = True

    if digit == 1 or 0:

        is_prime = False
   
    while start < digit:

        if digit % start == 0:

            is_prime = False

            break

        start = start + 1
   
    if is_prime:

        print(digit, "is a prime number")
      
    else:

        print(digit, "is not a prime number")

    n = n // 10
