n = int(input("Enter count of numbers:" + "\n"))

count = 1
lowest_number = 0

while count <= n:
    
    number = int(input("Enter number:" + "\n"))

    if number < lowest_number:

        lowest_number = number

    count += 1

print("The lowest number is:", lowest_number)

