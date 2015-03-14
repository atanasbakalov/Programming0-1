n = int(input("Enter count of numbers:" + "\n"))

count = 1
num_list = []
sum_numbers = 0

while count <= n:
    
    number = int(input("Enter number:" + "\n"))
    sum_numbers += number
    num_list = num_list + [number]

    count += 1

avg = (sum_numbers / len(num_list))

print("The average of all numbers is:", int(avg))

