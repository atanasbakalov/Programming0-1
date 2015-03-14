user1_number1 = input ("Потребител 1, моля въведете произволно число:" + "\n")
user1_number2 = input ("Потребител 1, моля въведете второ произволно число:" + "\n")
user_oper = input ("Въведете оператор" + "\n")


if user_oper == "+":
    
    print (int(user1_number1) + int(user1_number2))
    
elif user_oper == "-":
    
    print (int(user1_number1) - int(user1_number2))
    
elif user_oper == "*":
    
    print (int(user1_number1) * int(user1_number2))
    
elif user_oper == "/":
    
    print (int(user1_number1) / int(user1_number2))

else:

    print("Избрания от Вас оператор не се поддържа от програмата")


