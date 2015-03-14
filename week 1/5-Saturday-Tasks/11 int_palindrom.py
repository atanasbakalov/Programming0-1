n = int(input("Въведете произволно число" + "\n"))

m = n

reversed_num = 0

while n != 0:

    digit = n % 10

    reversed_num = reversed_num * 10 + digit

    n = n // 10

if reversed_num == m:

    print("Въведеното от Вас число е палиндром")

else:

    print("Въведеното от Вас число не е палиндром")
