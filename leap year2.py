year=int(input("Enter a year to check leap year or not:-"))
if year%400==0:
    print(year,"is an leap year")
elif year%100==0:
    print(year,"is not a leap year")
elif year%4==0:
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")
