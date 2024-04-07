#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill = input("enter bill ") 
tip = input("what % tip want to give ")
people = input("how many split ")

billnum = int(bill)
tipnum = int(tip)
total_bill = billnum + ((tipnum*billnum) / 100)

pay = total_bill / int(people)
payround = (f"{pay:.3f}")

print(f"each person should pay {payround}")
