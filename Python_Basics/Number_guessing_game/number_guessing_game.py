import random
import time

valu = random.randint(1, 50)


def game(value):
    for i in range(1, 11):
        if i == 1:
            guess = int(input('Enter your first guess::'))

        else:
            guess = int(input('Enter your next guess::'))

        if i <= 9:
            if guess == value:
                print(f'You Guessed the correct number and took {i} trails')
                exit()

            elif guess > value:
                print('Guess a lower value', end='          ')

            elif guess < value:
                print('Guess a higher value', end='          ')

            print(f'Remaining Guesses = {10-i}')
            time.sleep(1)

        else:
            print(f'You failed to guess the number. It was {value}')


game(valu)
