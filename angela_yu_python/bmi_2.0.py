height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
bmi_weight = round(weight / (height/100)**2)
if bmi_weight < 18.5:
    print(f"Your bmi is {bmi_weight} you are Underweight")
elif bmi_weight< 25:
     print(f"Your bmi is {bmi_weight} yay you are normal weight")
elif bmi_weight < 30:
    print(f"Your bmi is {bmi_weight} you are slightly overweight")
elif bmi_weight < 35:
    print(f"Your bmi is {bmi_weight} you are obese!")
else:
    print(f"Your bmi is {bmi_weight} you are clinically obese, Get Help!!")
