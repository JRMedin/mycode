#!/usr/bin/env python3
round = 0
while True:
    round = round + 1
    print('Finish the movie title, "Monty Python\'s The Life of ______"')
    answer = input("Your guess--> ")
    if answer.lower()  == 'brian':
        print('Correct')
        break
    elif answer == 'shrubbery':
        print('YOU HAVE FOUND THE SECRET ANSWER')
        exit(0)
        break
    elif round==3:
        print("Sorry, the answer was Brian.")
        break
    else:
        print("Sorry! Try again!")
round = 4
while True:
    round += 1
    print('Finish this line "Shake and ____"')
    answer = input("your guess--> ")
    if answer.lower() == 'bake':
        print('If you aint first youre last')
        break   
    elif round == 7:    # logic to ensure round has not yet reached 3
        print("Sorry, the answer was Bake.")
        break
    else:                 # if answer was wrong
        print("Sorry. Try again!")

