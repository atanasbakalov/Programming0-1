n = int(input("Enter count of numbers:" + "\n"))

count = 1
sum_evens = 0
list_evens = []

while count <= n:
    
    number = input("Enter number: ")
    number = int(number)

    if number % 2 == 0:
        
        sum_evens += 1
        list_evens += [number]

    count += 1

print("Count of evens:", sum_evens)
    
for item in list_evens:

    print("Evens are:")
    print(item)
