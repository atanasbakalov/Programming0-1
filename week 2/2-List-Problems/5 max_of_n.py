n = int(input("Enter count of numbers:" + "\n"))

count = 1
biggest_number = 0

while count <= n:
    
    number = int(input("Enter number:" + "\n"))

    if number > biggest_number:

        biggest_number = number

    count += 1

print("The biggest number is:", biggest_number)

