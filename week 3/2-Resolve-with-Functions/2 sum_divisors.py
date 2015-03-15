def sum_divisors(n):

    sum_divisors = 0

    start = 1

    while start < n:

        if n % start == 0:

            sum_divisors += start

        start += 1

    return sum_divisors

print(sum_divisors(12))
