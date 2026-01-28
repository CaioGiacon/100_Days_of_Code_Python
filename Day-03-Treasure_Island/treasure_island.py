print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/__/____
*******************************************************************************
''')


print('Welcome to Treasure Island.\nYour Mission is to find the treasure.')
cross_road = str(input('You\'re at a cross road. Where do you want to go?\nType "left" or "right" ').lower())

if cross_road == 'left':
    swim_or_wait = str(input('You\'ve come to a lake. There is a island in the middle of the lake. Do you want to swim or wait? ').lower())
    if swim_or_wait == 'wait':
        doors = str(input('You\'ve arrived at the island. Theres is 3 doors with different colors: Red, Yellow or Blue. Which color do you choose? ').title())
        if doors == 'Red':
            print('Burned by fire. GAME OVER!☠️')
        elif doors == 'Blue':
            print('Eaten by beasts. GAME OVER!☠️')
        elif doors == 'Yellow':
            print('YOU WIN! CONGRATULATIONS')
        else: 
            print('GAME OVER!☠️')
    else: 
        print('Attacked by trout. GAME OVER!☠️')
else:
    print('Fall into a hole. GAME OVER!☠️')