number1 = int(input("Въведете първо число" + "\n"))

number2 = int(input("Въведете второ число" + "\n"))

last_digit1 = number1 % 10
last_digit2 = number2 % 10

if last_digit1 > last_digit2:
    
    print("Числото с по-голяма последна цифра е:", number1)
    
elif last_digit1 < last_digit2:
    
    print("Числото с по-голяма последна цифра е:", number2)
    
else:
    
    if number1 > number2:
        
        print("Последните цифри на числата са еднакви,",
              number1, "е по-голямото число")

    else:

        print("Последните цифри на числата са еднакви,",
              number2, "е по-голямото число")
