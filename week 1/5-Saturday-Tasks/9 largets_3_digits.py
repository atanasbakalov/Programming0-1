n = int(input("Въведете число:" + "\n"))

x = n % 10

n = n // 10

y = n % 10
 
n = n // 10

z = n % 10

if x < y and x < z and y > z:

    smallest_number = x

    middle_number = z

    largest_number = y

if x < y and x < z and y < z:

    smallest_number = x

    middle_number = y

    largest_number = z 

elif x > y and x > z and y > z:

    largest_number = x

    middle_number = y

    smallest_number = z

elif x > y and x > z and y < z:

    largest_number = x

    middle_number = z

    smallest_number = y

elif x > y and x < z and y > z:

    middle_number = x

    largest_number = y

    smallest_number = z

elif x > y and x < z and y < z:

    middle_number = x

    largest_number = z

    smallest_number = y

largest_new = int(str(largest_number)+str(middle_number)+str(smallest_number))

smallest_new = int(str(smallest_number)+str(middle_number)+str(largest_number))

print("The smallest possible combination with these digits is:", smallest_new)

print("The biggest possible combination with these digits is:", largest_new)

    
