height = float(input("Enter your height in m: "))
weight = int(input("Enter your weight in kg: "))
bmi = round(weight / (height/100)**2,2)
print(f"Your height is {height}, your weight is {weight}, and your bmi is {bmi}")

#we can use f-string to print various daata types together using {}