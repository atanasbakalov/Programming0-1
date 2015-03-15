def is_perfect(n):

    is_perfect = True

    sum_divisors = 0

    start = 1

    while start < n:

        if n % start == 0:

            sum_divisors += start

        start += 1

    if sum_divisors != n:

        is_perfect = False

    return is_perfect

print(is_perfect(6))

print(is_perfect(28))

print(is_perfect(496))

print(is_perfect(50))

print(is_perfect(88))
