print("It's a tip generator!")
total = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))  

print("Each person should pay: $", (total + (total * tip / 100)) / people)