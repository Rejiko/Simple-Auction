import replit
import art

bidders = {}
print(art.logo)
print("Welcome to the secret auction program.")

max_bid = 0
finished_bidding = False

while not finished_bidding:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidders[name] = bid
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.")
    if should_continue == "no":
        finished_bidding = True
    elif should_continue == "yes":
        replit.clear()

for i in bidders:
    if bidders[i] > max_bid:
        max_bid = bidders[i]
        bidder = i

print(f"The winner is {bidder}, with a bid of ${max_bid}")