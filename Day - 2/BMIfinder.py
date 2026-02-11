print("Find your BMI")
h = float(input("Enter your height in m: "))
w = float(input("Enter your weight in kg: "))

bmi = w / (h ** 2)

print("Your BMI is " + str(bmi))