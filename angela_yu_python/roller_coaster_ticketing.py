print("Welcome to the rollercoaster !!")
height = int(input("Enter your height in cm : "))

if height >= 120:
    print("You can ride the roller coaster!!")
    age = int(input("Enter your age : "))
    if age < 12:
        bill = 5
        print("Childrens pay $5")
    elif age <= 18:
        bill = 7
        print("Youth pay $7")
    else:
        bill = 12
        print("Adults pay $12")
    wants_photo=input("Do you want photos taken? Y or N: ")
    if wants_photo == "Y":
        bill += 3
    print(f"Your final bill is {bill}")
else:
    print("oops,You have to grow taller before you can ride !!")