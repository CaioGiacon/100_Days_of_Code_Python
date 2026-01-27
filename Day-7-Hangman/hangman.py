import random
from hangman_stages import stages, art
from world_list import word_list

chosen_word = random.choice(word_list)

print(art)

game_over = False
correct_letters = []
lives = 6
while not game_over:
    
    print(f'****************************{lives}/6 LIVES LEFT****************************')
    guess = input('Guess a letter: ').lower()
    
    if guess in correct_letters:
        print(f'You\'ve already guessed {guess}')

    display = ''
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += '_'
    
    if guess not in chosen_word:
        lives -= 1
        print(f'You guessed {guess} that\'s not in the word. You lose a life')
        if lives == 0:
            game_over = True
            print(f'********************IT WAS {chosen_word}! YOU LOSE********************')
    if '_' not in display:
        game_over = True
        print('********************YOU WIN********************')
   
    print(display)

    print(stages[lives])
    