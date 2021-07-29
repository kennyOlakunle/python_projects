import random


def guess_num(x):
    random_num = random.randint(1, x)
    guess = 0

    while guess != random_num:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_num:
            print('Sorry, guess again. Too low')
        elif guess > random_num:
            print("Sorry, guess again. Too high.")

    print(f"Yay. You have guessed the number {random_num} correctly")


guess_num(10)
