rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
RPS = [rock , paper ,scissors]
import random 

choose = int(input("enter 1 for rock 2 for paper 3 for scissors \n"))
print (f"you choose {RPS[choose-1]} ")
comp_choose = random.randint(1,3)

print(f"computer choose {RPS[comp_choose-1]}")

if choose == 1 and comp_choose ==3:
  print("user wins")
elif comp_choose==1 and choose == 3:
  print("computer wins")
elif comp_choose < choose :
  print("user wins")


elif choose < comp_choose :
  print("computer wins")

elif choose == comp_choose :
  print("draw")

