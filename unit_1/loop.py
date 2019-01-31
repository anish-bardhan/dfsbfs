guess = int(input("\nyou have eight tries. \n\nguess a number 1-25?"))
num = 14
count = 1

while guess != num and count < 8:
    if guess > num:
        print("\ntoo high, guess again!")
        guess = int(input("\nwhat's the number?"))
    elif guess < num:
        print("\ntoo low, guess again!")
        guess = int(input("\nwhat's the number?"))
    count = count + 1
if guess == num:
    print("\nyou got it!\n")
if count == 8:
    print("you lose!")
