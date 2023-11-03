#Assignment statement
num1 = 9
num2 = 30

#expression statement
result = num1+num2

#print statement
print(result)

#input statement
#name = input("Enter your name: ")
#print(name)

#Conditional statements (if, elif, else)
if num1>10:
    print("num1 is greater than 10")
elif num1==10:
    print("num1 is equal to 10")
else:
    print("num1 is less than 10")

#while loop
print("While Loop")
count = 5
while count>=1:
    print(count)
    count -= 1 #increment or decrement

#for loop
print("For loop")
for i in range(10,1,-2):
    print(i)


#function
#syntax: def function_name(parameters1, p2):
    #statement
def addition(a, b):
    return a + b

result = addition(15, 17)  #calling the function
print(result)

#exception handling using try,except,finally
try:
    remainder = 10/0
    print(remainder)
except ZeroDivisionError as e:
    print("Cannot divide a number by zero")
finally:
    print("Always gets executed")


#list
number_list = [1,2,3,4,5]
print(number_list)
print(type(number_list))
number_list.append(7) #add an element to the list
print(number_list)

'''
This is an
example of multi line comment
'''

try:
    num3 = int(input("Enter first number: "))
    num4 = int(input("Enter second number: "))

    print(type(num3))

    result = addition(num3,num4)
    print(result)
    
except ValueError:
    print("Invalid Input!!")


def division(a ,b):
    return a/b

try:
    num3 = int(input("Enter first number: "))
    num4 = int(input("Enter second number: "))

    print(type(num3))

    result = division(num3,num4)
    print(result)
    
except ValueError:
    print("Invalid Input!!")

except ZeroDivisionError:
    print("Cannot divide a number by zero")