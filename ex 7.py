

###############################################################################
#  Program Name   : Program Name Ex.7py
#  Author         : Your Name
#  Task           : (Write a program that asks for two numbers and prints the larger one)
#  Date           : Date
###############################################################################

age = int(input("Enter your age: "))
if age >= 16:
    print("You are old enough to drive.")
    if age == 16:
        print("Amazing.")
else:
    print("Are you in grade 11.")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    print("The larger number is:", num1)
elif num2 > num1:
    print("The larger number is:", num2)
else:
    print("Both numbers are equal.")

        
