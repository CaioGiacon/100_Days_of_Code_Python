from art import LOGO, VS
from game_data import data
import random
import os

A = random.choice(data)
B = random.choice(data)
USER_SCORE = 0

user_guess_is_right = True
while user_guess_is_right:
    print(LOGO)
    print(f'Current Score: {USER_SCORE}')
    print(f'Compare A: {A['name']}, {A['description']}, from {A['country']}.')
    print(VS)
    print(f'Compare B: {B['name']}, {B['description']}, from {B['country']}.')

    more_followers = input('Who has more followers? Type "A" or "B": ').upper()

    if more_followers == 'A':
        if A['follower_count'] > B['follower_count'] or A['follower_count'] == B['follower_count']:
            USER_SCORE += 1
            A = B
            B = random.choice(data)
            os.system('cls')
        else:
            os.system('cls')
            print(LOGO)
            print(f'Sorry, that\'s wrong. Final score: {USER_SCORE}')
            user_guess_is_right = False
    elif more_followers == 'B':
        if B['follower_count'] > A['follower_count'] or A['follower_count'] == B['follower_count']:
            USER_SCORE += 1
            A = B
            B = random.choice(data)
            os.system('cls')
        else:
            os.system('cls')
            print(LOGO)
            print(f'Sorry, that\'s wrong. Final score: {USER_SCORE}')
            user_guess_is_right = False
    else:
        os.system('cls')
        print(LOGO)
        print(f'Sorry, that\'s wrong. Final score: {USER_SCORE}')
        user_guess_is_right = False