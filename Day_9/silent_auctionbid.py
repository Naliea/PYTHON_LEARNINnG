from clear import clear
from art import logo
print(logo)
print("Welcome to the secret auction program.")
#Silent Auction Program
user_dict = {}
game_over = True
while game_over:
    user_name = input("Enter your name: ")
    user_bid = int(input("Enter your bid: $"))
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    user_dict[user_name] = user_bid
    if other_bidders.lower() == 'no':
        clear()
        #Calculating the highest bid
        winner = ""
        max_bid = max(user_dict.values())
        for name in user_dict:
            if user_dict[name] == max_bid:
                winner = name
        print(f"The winner is {winner} with a bid of {max_bid}")
        game_over = False
    elif other_bidders.lower() == 'yes':
        clear()
#Things I havent implemented:
# 1. Validation of inputs:Valid bid,other bidders, etc.
#2.Simplifying the Highest bid calculation
