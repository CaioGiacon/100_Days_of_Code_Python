import random
import os
from art import logo

def deck_sum(deck):
    if sum(deck) == 21 and len(deck) == 2:
        return 0
    if 11 in deck and sum(deck) > 21:
        deck.remove(11)
        deck.append(1)
    return sum(deck)
 
def final(user_deck, computer_deck):
    print(f'Your final hand: {user_deck}, final score: {deck_sum(user_deck)}')
    print(f'Computer\'s final hand: {computer_deck}, final score {deck_sum(computer_deck)}')

def blackjack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_deck = random.choices(cards, k=2)
    computer_deck = random.choices(cards, k=2)
    
    print(logo)
    play_game = True
    while play_game:
        
        print(f'Your cards {user_deck}, current score: {deck_sum(user_deck)}')
        print(f'Computer\'s first card: {computer_deck[0]} ')
        another_card = input('Type "y" to get another card, type "n" to pass: ')

        if another_card == 'y':
            user_deck.append(random.choice(cards))
            deck_sum(user_deck)
            if deck_sum(user_deck) > 21:
                final(user_deck, computer_deck)
                print('You went over. You lose 😭')
                play_game = False

        elif another_card == 'n':
            computer_still_play = True
            while computer_still_play:
                computer_choice = random.choice(['y', 'n'])
                if computer_choice == 'y':
                    computer_deck.append(random.choice(cards))
                    deck_sum(computer_deck)
                    if deck_sum(computer_deck) > 21:
                        final(user_deck, computer_deck)
                        print('You win 😃')
                        computer_still_play = False
                        play_game = False
                elif computer_choice == 'n':
                    if deck_sum(user_deck) == deck_sum(computer_deck):
                        final(user_deck, computer_deck)
                        print('It\'s a draw')
                    elif deck_sum(user_deck) > 21 and deck_sum(computer_deck) < 21:
                        final(user_deck, computer_deck)
                        print('You went over. You lose 😭')
                    elif deck_sum(user_deck) < 21 and deck_sum(computer_deck) > 21:
                        final(user_deck, computer_deck)
                        print('You win 😃')
                    elif deck_sum(user_deck) < deck_sum(computer_deck):
                        final(user_deck, computer_deck)
                        print('You went over. You lose 😭')
                    elif deck_sum(user_deck) > deck_sum(computer_deck):
                        final(user_deck, computer_deck)
                        print('You win 😃')
                    elif deck_sum(user_deck) == 11 or deck_sum(computer_deck) == 11:
                        final(user_deck, computer_deck)
                        print('Win with a blackjack')
                        

                    computer_still_play = False
            play_game = False
    return user_deck, computer_deck


while input('Do you want to play a game of Blackjack? Type "y" or "n":') == 'y':
    os.system('cls')
    blackjack()