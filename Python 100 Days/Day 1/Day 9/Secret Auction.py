from replit import clear
from art import logo
print("Secret Auction Bid\n")
print(logo)

still_bidding = True
bidding_dict = {}
highest_bidder = 0.0
while still_bidding:
    name = input("What is your name?: ").title()
    bid = float(input("What's your bid amount?: $"))
    bidding_dict[name] = bid

    question = input('Are there any other bidders? Type y for Yes and n for No: ').lower()

    if question == 'y':
        clear()
    else:
        still_bidding = False

    for key in bidding_dict:
        if bidding_dict[key] > highest_bidder:
            highest_bidder = bidding_dict[key]

print(bidding_dict)
print(f'The winner of the bid is {key} with bid value ${highest_bidder}')
