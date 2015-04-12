i = int(input("Enter an odd number:" + "\n"))

while i % 2 != 1:
    print(i, "is not an odd number. Enter an odd number !")
    i = int(input("Enter an odd number:" + "\n"))

stars = "*"
dots = "."
number_dots = 1
number_stars = i
        
should_reverse = False

for y in range(0, i):
    print ((number_dots*dots)
        + (stars * number_stars)
        + (number_dots*dots))

    if should_reverse:
        number_stars += 2
        number_dots -= 1
    else:
        number_dots += 1
        number_stars -= 2

    if number_stars == 1:
        should_reverse = True
