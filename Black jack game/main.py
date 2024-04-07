import random
from replit import clear
from art import logo

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

def calc_score(cards):
    """calculates card selected score"""
    
    if sum(cards) ==21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score,comp_score):
    if user_score == comp_score:
        print("Draw")

    elif comp_score == 0:
        print("Computer wins")

    elif user_score==0:
        print("you win")

    elif user_score>21:
        print("you went over,you loses")
    elif comp_score>21:
        print("computer went over,computer loses")

    else:
        if user_score>comp_score:
            print("you wins")
        else:
            print("computer wins")
def deal_cards():
    """returns a card randomly from deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,]
    card_selected = random.choice(cards)
    return card_selected



def play_game(): 
    print(logo)
    user_card = []
    computer_card = []
    user_score = calc_score(user_card)
    comp_score = calc_score(computer_card)
        
    for _ in range(2):
       
        user_card.append(deal_cards())
        computer_card.append(deal_cards())
        
    is_game_over = False

    while not is_game_over:
        user_score = calc_score(user_card)
        comp_score = calc_score(computer_card)
        print(f"Your cards: {user_card} ,current score: {user_score}" )
        print(f"computer cards: {computer_card[0]}")
    
        if user_score ==0 or comp_score == 0 or user_score >21:
            is_game_over = True
        else:
            another_card = input("You want to draw another card?y/ n  ")
            if another_card == "y":
                user_card.append(deal_cards())
                user_score = calc_score(user_card)
            else:
                is_game_over = True
    while comp_score !=0 and comp_score<17:
        computer_card.append(deal_cards())
        comp_score = calc_score(computer_card)
    print(f"Your final cards: {user_card} ,final score: {user_score}" )
    print(f"computer final cards: {computer_card},computer final score:{comp_score}")
    compare(user_score,comp_score)
    

while input("Do you want to start a new game? y/n: ") == "y":
   
    clear()
    play_game()
    




