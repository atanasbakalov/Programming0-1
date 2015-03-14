n = int(input("Въведете произволно число:" + "\n"))

sum_digits = 0

while n != 0:
    
    digit = n % 10
    
    sum_digits = sum_digits + digit
    
    n = n//10
    
print("Сумата на цифрите на числото Ви е равна на:", sum_digits)
