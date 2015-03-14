n = int(input("Въведете общия брой точки от теста" + "\n"))

min = 0

max = 100

if n <= 50:

    print("Слаб 2")

if n > 50 and n <= 60:

    print("Среден 3")

if n > 60 and n <= 70:

    print("Добър 4")

if n > 70 and n <= 80:

    print("Мн.добър 5")

if n >80 and n <= 99:

    print("Отличен 6")

if n == 100:

    print("Много отличен 7")
