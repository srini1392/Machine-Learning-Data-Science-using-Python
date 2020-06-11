### Title           :myCalculator.py
### Author          :Srinikethan M
### Date & Time     :019-06-03 14:46:02

def add(x,y):
    ''' this function returns the sum of 2 numbers entered'''
    return x+y

def multiply(x,y):
    ''' this function returns the multiplication of 2 numbers entered'''
    return x*y

def divide(x,y):
    ''' this function returns the division of 2 numbers entered'''
    return x/y

def subtract(x,y):
    ''' this function returns the subtraction of 2 numbers entered'''
    return x-y

# take input from user
print("Select the desired operation")
print("1. Add")
print("2.Multiply")
print("3.Divide")
print("4.Subtract")

choice = input("enter choice (1/2/3/4):")

num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))

if choice == '1':
    print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
    print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '3':
    print(num1,"/",num2,"=", divide(num1,num2))

elif choice == '4':
    print(num1,"-",num2,"=", subtract(num1,num2))

else:
    print("invalid input")

