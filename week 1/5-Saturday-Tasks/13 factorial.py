n = int(input("Enter a number" + "\n"))

start = 1

factorial = 1

if n == 0:

    factorial = 1

else:

    while start <= n:

        factorial = factorial * start

        start += 1

print("Factorial is:", factorial)
