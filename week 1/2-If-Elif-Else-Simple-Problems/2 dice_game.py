dice_sides = int(input("Въведете брой на страните на зарчето:" + "\n"))
player1_name = input ("Името на Играч 1 е:" + "\n")
player2_name = input ("Името на Играч 2 е:" + "\n")

from random import randint

dice1 = randint (1, dice_sides)

print("Зарчето на", player1_name, "падна на", dice1)

dice2 = randint (1, dice_sides)

print("Зарчето на", player2_name, "падна на", dice2)


if dice1 > dice2:
    print (player1_name, "победи !")
    
elif dice1 == dice2:
    print (player1_name, "и" , player1_name, "са равни!")
    
else:
    print (player2_name, "победи !")


