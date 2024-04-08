from art import logo
from art import vs
from game_data import data
import random
from replit import clear

def select_celeb():
    selected = random.choice(data)
    return selected
    
def compare(followersone,followerstwo,user_input):
    
    if followersone > followerstwo and user_input == "a" or  followersone < followerstwo and user_input == "b":
        return 0
    else:
        return 1

def game():
     print(logo)
    
     one_selected = select_celeb()
     print(f"compare : {one_selected['name']}, {one_selected['description']}, from {one_selected['country']}")
     followersone = one_selected["follower_count"]
    
     print(vs)
    
     two_selected = select_celeb()
     print(f"against : {two_selected['name']}, {two_selected['description']}, from {two_selected['country']}")
     followerstwo = two_selected["follower_count"]
     
     is_right = True
     score = 0
     while is_right:
        user=input("Who one has more followers? type A or B ").lower()
        answer = compare(followersone,followerstwo,user)
        
        if answer == 0:
           clear()
           print(logo)
           score +=1
           print(f"you are right! , current score {score}")
           one_selected = two_selected
           print(f"compare : {one_selected['name']}, {one_selected['description']}, from {one_selected['country']}")
          
           followersone = one_selected["follower_count"]
           two_selected = select_celeb()
           if one_selected == two_selected:
               two_selected = select_celeb()
           print(vs)
           print(f"against : {two_selected['name']}, {two_selected['description']}, from {two_selected['country']}")
           
           followerstwo = two_selected["follower_count"]
           compare(followersone,followerstwo,user)
        elif answer == 1:
            is_right = False
            print(f"Game over, final score is {score}")


game()
