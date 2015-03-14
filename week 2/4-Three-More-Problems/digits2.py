x = int(input("Type a number" + "\n"))

digits = []

while x != 0:
    digit = x % 10
    digits = [digit] + digits
    x = x // 10

print("List of digits is:", digits)

y = 0

for digit in digits:
    y = y * 10 + digit
    print(y)

    
