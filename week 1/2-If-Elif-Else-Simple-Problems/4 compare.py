user1_number1 = int(input("Потребител 1, моля въведете произволно число:"
                          + "\n"))
user1_number2 = int(input("Потребител 1, моля въведете второ произволно число:"
                       + "\n"))

if user1_number1 > user1_number2:
    
    print (user1_number1, "е по-голямо от", user1_number2)
    
elif user1_number1 == user1_number2:
    
    print (user1_number1, "е равно на", user1_number2)

else:
    
    print (user1_number2, "е по-голямо от", user1_number1)
    


