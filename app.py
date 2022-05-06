import random


#   Dice comparison and winner announcer function
def dice_logic():
    if dicenumber_off == 3 and dicenumber_def == 2:

        if defence[0] >= offence[0] and defence[1] >= offence[1]:
            print("Offence lose both units")

        elif offence[0] > defence[0] and offence[1] > defence[1]:
            print("Defence lose both units")

        else:
            print("Both lose one unit")

    if dicenumber_off == 2 and dicenumber_def == 2:

        if defence[0] >= offence[0] and defence[1] >= offence[1]:
            print("Offence lose both units")

        elif offence[0] > defence[0] and offence[1] > defence[1]:
            print("Defence lose both units")

        else:
            print("Both lose one unit")

    if dicenumber_def == 1:
        if defence[0] >= offence[0]:
            print("Offence lose one unit")

        elif offence[0] > defence[0]:
            print("Defence lose one unit")


#   Initializing and declaring variables for lists with random numbers and no-value variables for dice input
offence = [str(random.randint(1, 6)), str(random.randint(1, 6)), str(random.randint(1, 6))]
defence = [str(random.randint(1, 6)), str(random.randint(1, 6))]
dicenumber_off = None
dicenumber_def = None

#   sorting lists - descending
offence.sort(reverse=True)
defence.sort(reverse=True)

#   loop to make sure that player input is valid
while True:
    try:
        dicenumber_off = int(input("Choose dice number for strike (1-3): "))
        if dicenumber_off <= 3:
            break

    except ValueError:
        if dicenumber_off > 3:
            continue
        continue

while True:
    try:
        dicenumber_def = int(input("Choose dice number for defence (1-2): "))
        if dicenumber_def <= 2:
            break

    except ValueError:
        if dicenumber_def > 2:
            continue
        continue

#  Rolled dice visual
if dicenumber_off == 3:
    print("Offence: " + offence[0] + " " + offence[1] + " " + offence[2])


elif dicenumber_off == 2:
    print("Offence: " + offence[0] + " " + offence[1])


elif dicenumber_off == 1:
    print("Offence: " + offence[0])

if dicenumber_def == 2:
    print("Defence: " + defence[0] + " " + defence[1])

elif dicenumber_def == 1:
    print("Defence: " + defence[0])

print("------------")
dice_logic()
