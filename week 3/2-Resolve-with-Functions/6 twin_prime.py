def twin_prime(n):
    
    start = 2

    is_prime = True

    if n == 1 or 0:

        is_prime = False
       
    while start < n:

        if n % start == 0:

            is_prime = False

            break

        start = start + 1
       
    if is_prime:

        m = n + 2

        is_prime_twin = True

        if m == 1 or 0:

            is_prime_twin = False
       
        while start < m:

            if m % start == 0:

                is_prime_twin = False

                break

            start = start + 1

    if is_prime and is_prime_twin:

        print(n, "and", m, "are prime twins")
          
    else:

        print(n, "has no prime twin")

    n = n // 10

print(twin_prime(5))
print(twin_prime(7))
print(twin_prime(28))
