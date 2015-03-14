n = int(input("Въведете край на интервала" + "\n"))

start = 0

sum_evens = 0

while start <= n:

    if start %2 == 0:

        sum_evens += start

    start += 1

print("Сумата на всички четни числа в интервала е равна на:", sum_evens)
