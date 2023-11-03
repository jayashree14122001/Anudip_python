side1= 5
side2= 6
side3= 7

# calculate the semi-perimeter
s = (side1+ side2 + side3) / 2

# calculate the area
area = (s*(s-side1)*(s-side2)*(s-side3)) ** 0.5

print("The area of the given triangle is %0.2f" %area)

#output
#The area of the triangle is 14.70