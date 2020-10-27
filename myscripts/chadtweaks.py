#!/usr/bin/env python3


print('Welcome to Will Ferrell Movie Trivia. Tonight you will guess the following quotes for a chance to win our Grand prize!')

print('For our first quote please name the film it came from "If you aint first your last!"')
answer = input("Your guess--> ")
if answer.lower() == 'talladega nights':
    print('Good Job!')
else:
    print('Sorry! The Answer was actually Talladega nights')

print('For our second question try to guess this film "At age 11, I audited my parents. Believe me, there were some discrepancies, and I was grounded"')

answer = input("Your guess--> ")
if answer.lower() == 'the other guys':
    print('Nice Work!')
else:
    print('Need to watch some more movies and try again')
    
print('The third and final quote for the Grand prize guess this film to win. "Its the ****ing Catalina Wine Mixer" remember you only get one guess and no calling tom cruise for help')

answer = input("Your guess--> ")
if answer.lower() == 'step brothers':
    print("Congratulations!")
else:
    print("WRONG!")

