# Taking kilometers input from the user
kilometers = float(input("Enter value in kilometers to convert it into miles: "))

# conversion factor
conv_fac = 0.621371

# calculate miles
miles = kilometers * conv_fac
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))

#Enter value in kilometers to convert it into miles: 15
#15.00 kilometers is equal to 9.32 miles