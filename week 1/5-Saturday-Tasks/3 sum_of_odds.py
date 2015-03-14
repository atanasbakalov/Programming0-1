n = int(input("Въведете край на интервала" + "\n"))

start = 0

sum_odds = 0

while start <= n:

    if start %2 == 1:

        sum_odds += start

    start += 1

print("Сумата на всички четни числа в интервала е равна на:", sum_odds)
