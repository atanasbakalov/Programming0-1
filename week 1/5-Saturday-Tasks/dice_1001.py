turns_ivan = 5

turns_maria = 5

sum_ivan = 1001

sum_maria = 1001

counter_turns_ivan = 0

counter_turns_maria = 0

from random import randint

dice_roll = randint(1, 6)

while sum_ivan != 0:

    start1 = 1

    if sum_ivan >= 0:

        while start1 <= turns_ivan:

            dice_roll = randint(1, 6)

            sum_ivan -= dice_roll

            start1 += 1

            counter_turns_ivan += 1

    else:

        while start1 <= turns_ivan:

            dice_roll = randint(1, 6)

            sum_ivan += dice_roll

            start1 += 1
            
            counter_turns_ivan += 1
    
    print("Middle score of Ivan is:", sum_ivan)

print("--------------------------------------------------")

print("Ivan reached 0 at his", (str(counter_turns_ivan)+"th"), "roll")

print("--------------------------------------------------")


while sum_maria != 0:

    start2 = 1

    if sum_maria >= 0:

        while start2 <= turns_maria:

            dice_roll = randint(1, 6)

            sum_maria -= dice_roll

            start2 += 1

            counter_turns_maria += 1

    else:

        while start2 <= turns_maria:

            dice_roll = randint(1, 6)

            sum_maria += dice_roll

            start2 += 1
            
            counter_turns_maria += 1
    
    print("Middle score of Maria is:", sum_maria)

print("--------------------------------------------------")

print("Maria reached 0 at her", (str(counter_turns_maria)+"th"), "roll")

print("--------------------------------------------------")

if counter_turns_ivan > counter_turns_maria:

    print("Maria reached 0 first ! Maria is the winner !")

else:

    print("Ivan reached 0 first ! Ivan is the winner !")



