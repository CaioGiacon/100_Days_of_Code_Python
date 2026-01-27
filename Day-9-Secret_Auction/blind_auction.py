import os
from art import logo

print(logo)

def highest_bidder(bidding_dictionary):
    highest_bid = max(bidding_dictionary.values())
    winner = max(bidding_dictionary, key=bidding_dictionary.get)
       
    print(f'The winner is {winner} with a bid of ${highest_bid}')

other_bidders = True
auction_dict = {}  
while other_bidders:
    name = input('What is your name?: ').title()
    price = int(input('What is your bid?: $'))
    
    auction_dict[name] = price
        
    bidders = input('Are there any other bidders? Type "yes or no".\n').lower()
    if bidders == 'no':
        other_bidders = False
        highest_bidder(auction_dict)
    else:
        os.system('cls')


