print("Welcome to the tip calculator !")
total = float(input("Enter the total bill : $"))
tip = int(input("What percentage tip would you like to give? 10,12 or 15 : "))
split = int(input("How many people to split the bill : "))
tip_percent = total*tip/100
split_bill = round((total+tip_percent)/split,2)
print(f"Each person has to pay ${split_bill}")


