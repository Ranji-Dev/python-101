year = int(input("Enter the year : "))
if year % 4 ==0 and year % 100 != 0:
    print(f"The {year} is an leap year")
elif year % 400 ==0:
    print(f"The {year} is an leap year")
else:
    print(f"The {year} is not an leap year")