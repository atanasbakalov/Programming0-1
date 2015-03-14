lower_bound = int(input("Въведете долна граница на интвревала" + "\n"))
upper_bound = int(input("Въведете горна граница на интвревала" + "\n"))

while lower_bound <= upper_bound:

    if lower_bound % 2 == 0:

        print(lower_bound, "is even")

    else:

        print(lower_bound, "is odd")

    lower_bound += 1
