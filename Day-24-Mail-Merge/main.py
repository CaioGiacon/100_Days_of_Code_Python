from letter_functions import cleaning_letter, personalized_and_save_letter

with open('Input/Letters/starting_letter.txt') as letter:
    letter = letter.read()

with open('Input/Names/invited_names.txt') as n:
    g_names = n.readlines()

formated_letter = cleaning_letter(user_letter=letter, caracter_target='[', choose_replacement='')
formated_letter = cleaning_letter(user_letter=formated_letter, caracter_target=']', choose_replacement='')

personalized_and_save_letter(save_path='./Output/ReadyToSend/letter_for_', target='name', 
                    letter=formated_letter, names=g_names)