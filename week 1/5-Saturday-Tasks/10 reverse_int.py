n = int(input("Въведете число" + "\n"))

reversed_n = 0

while n != 0:
    digit = n % 10
    reversed_n = reversed_n * 10 + digit
    n = n // 10

print("Reversed number is:", reversed_n)
