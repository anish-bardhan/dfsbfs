import random
playing = True
while playing == True:
    if sum == 7 or sum == 11:
        print("winner")
        play = False
    elif sum == 2:
        print("loser")
        play = False
    else:
        print("keep going")
        dice1 = random.randint(1,6)
        print(dice1)
        dice2 = random.randint(1,6)
        print(dice2)
        print("your sum:")
        print(dice1 + dice2)
