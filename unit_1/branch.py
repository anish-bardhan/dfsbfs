print("you're teacher is checking homework which you didn't do. \ntry and avoid having homework checked. \nanswer with yes or no.")
# i made a staring text
ans = input("the teacher askes did you do your homework. \nhow do you respond?")
# i added an input so that user info can be added
if ans=="no":
    print("you've just given yourself away!")
if ans=="yes":
    print("good, but he isn't buying it.")
    ans = input("the teacher askes if you can show him your homework. \nhow do you respond?")
    if ans=="no":
        print("you've just given yourself away!")
    if ans=="yes":
        print("you flick through some random papers. he is now wondering where it is.")
        ans = input("the teacher tries to examine your backpack. \nhe askes that you open it for him, \nhow do you respond?")
        if ans=="no":
            print("he knows your hiding something. you've just given yourself away!")
        if ans=="yes":
            print("he looks through it with you and finds nothing.")
            ans = input("sarcastically, he askes if you think you may have forgot it at home, \nhow do you respond?")
            if ans == "no":
                ans = input("since it is lost, the teacher askes if you can make new copy by tomorrow, \nhow do you respond?")
                if ans=="no":
                    print("you've just wasted your second chance!")
                if ans=="yes":
                    print("not avoided, but not in trouble - a fair compromise")
            if ans == "yes":
                print("the teacher doesn't exactly know what to say.")
                ans = input("the teacher askes if you did part two, \nhow do you respond?")
                if ans=="yes":
                    print("there was no part two! you've just given yourself away!")
                if ans=="no":
                    print("at least you know what the assignment was.")
                    ans = input("the teacher askes if your dog ate your homework. \nhow do you respond?")
                    if ans=="yes":
                        print("you told him your dog didn't eat it, but your computer did")
                        ans = input("the teacher gives up, he would like to know if you can have it for tomorrow? \nhow do you respond?")
                        if ans=="no":
                            print("you were so close but you blew it!")
                        if ans=="yes":
                            print("you've just wasted your second chance!")
                    if ans=="no":
                        input("the teacher askes if you can you find it by the end of the day. \nhow do you respond?")
                        if ans=="no":
                            print("you've just wasted your second chance!")
                        if ans=="yes":
                            print("the teacher says you can turn it in for full credit. \ncongratulations, you've successfully outsmarted the teacher.")



# i used a loop so that if the wrong answer was submitted, the question would not progress


# use quit statements and end game if yes or no is not used as the answer
