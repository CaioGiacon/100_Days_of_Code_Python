import random
import templates


possible_choices = [templates.rock, templates.paper, templates.scissors]
user_choice = str(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n').lower())
computer_choice = random.choice(possible_choices)

if user_choice == '0':
    print(f'Users Choice: \n{possible_choices[0]}')
    if computer_choice == possible_choices[0]:
        print(f'Computers Choice: \n{computer_choice}')
        print('It\'s a draw')
    elif computer_choice == possible_choices[1]:
        print(f'Computers Choice: \n{computer_choice}')
        print('You lose')
    else:
        print(f'Computers Choice: \n{computer_choice}')
        print('You Win')

elif user_choice == '1':
    print(f'Users Choice: \n{possible_choices[1]}')
    if computer_choice == possible_choices[0]:
        print(f'Computers Choice: \n{computer_choice}')
        print('You Win')
    elif computer_choice == possible_choices[1]:
        print(f'Computers Choice: \n{computer_choice}')
        print('It\'s a draw')
    else:
        print(f'Computers Choice: \n{computer_choice}')
        print('You lose')

elif user_choice == '2':
    print(f'Users Choice: \n{possible_choices[2]}')
    if computer_choice == possible_choices[0]:
        print(f'Computers Choice: \n{computer_choice}')
        print('You lose')
    elif computer_choice == possible_choices[1]:
        print(f'Computers Choice: \n{computer_choice}')
        print('You Win')
    else:
        print(f'Computers Choice: \n{computer_choice}')
        print('It\'s a draw')
else:
    print('You typed a invalid number. You lose')

