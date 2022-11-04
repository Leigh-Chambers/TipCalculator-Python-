#Tip Calculator - project

#Test: If the bill was $150.00, split between 5 people, with 12% tip. 

#Expected outcome
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Note there are 2 ways to round a number.

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

split = (bill * (1+(tip/100)))/people 
print(f"Each person should pay: ${split:.2f}")