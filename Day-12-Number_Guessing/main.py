from random import randint
from art import logo

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5
RANDOM_NUMBER = randint(1, 100)

def set_difficulty(difficulty):
    if difficulty == 'easy':
        print(f'You have {EASY_ATTEMPTS} attempts remaining to guess the number.')
        make_guess(EASY_ATTEMPTS)
    elif difficulty == 'hard':
        print(f'You have {HARD_ATTEMPTS} attempts remaining to guess the number.')
        make_guess(HARD_ATTEMPTS)
    else:
        print('Invalid option')

def make_guess(user_attempt):
    while user_attempt > 0:
        user_guess = int(input('Make a guess: '))

        if user_attempt == 1:
            user_attempt = 0  
            print(f'You\'ve run out of guesses. Refresh the page to run again. The correct number was {RANDOM_NUMBER}')    
        elif user_guess == RANDOM_NUMBER: 
            print(f'You got it! The answer was {RANDOM_NUMBER}.')
            user_attempt = 0
        elif user_guess > RANDOM_NUMBER:
            user_attempt -= 1  
            print('Too high\nGuess again')
            print(f'You have {user_attempt} attempts remaining to guess the number.')
        elif user_guess < RANDOM_NUMBER:
            user_attempt -= 1  
            print('Too low\nGuess again')
            print(f'You have {user_attempt} attempts remaining to guess the number.')
            

print(logo)
print('Welcome to the Number Guessing Game!')
print('I\'m thinking of a number betweeen 1 and 100')
set_difficulty(input('Choose a difficulty. Type "easy" or "hard": ').lower())