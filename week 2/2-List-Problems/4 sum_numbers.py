n = int(input("Enter count of numbers:" + "\n"))

start = 1
sum_numbers = 0

while start <= n:
    
    number = int(input("Enter number:" + "\n"))

    sum_numbers += number

    start += 1

print("The sum of all numbers is:", sum_numbers)

