import random

def guess():
    levels = {"easy": 10, "medium": 5, "hard": 3}
    choice = input("Select a level: easy, medium or hard: ")

    attempts = levels[choice]
    chosen = random.randint(1, 100)
    tries = 0

    print(f'You have {attempts} attempts')
    while( tries < attempts):
        curr = int(input('Guess a number:'))
        if(curr < chosen):
            print('Too low')
        elif(curr > chosen):
            print('Too high')
        else:
            print('Congrats! You have guessed the number.')
            return
        tries += 1
        if(attempts-tries == 0):
            print('Out of attempts. Number was '+ str(chosen))
            return
        else:
            print('You have '+ str(attempts-tries) +' attempts')

if(__name__ == '__main__'):
    guess()