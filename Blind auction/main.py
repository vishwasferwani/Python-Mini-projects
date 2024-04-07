from replit import clear

from art import logo

print(logo)

print("Welcome to secret auction.")
bidders={}

more = True
while more :
    name = input("What is your name. ")
    bid = int(input("What is your bid.$"))
    bidders[name] = bid
    more = input("are there more bidders yes/no ")
    clear()
    if more == "no":
     more = False
        
def find_highest(bidding_record):
    highest = 0
    for all in bidders:
        bidding_amount= bidders[all]
        if bidding_amount>highest:
            highest= bidding_amount
            name = all
    print(f"winner is {name} with highest bid ${highest}")

find_highest(bidders)
