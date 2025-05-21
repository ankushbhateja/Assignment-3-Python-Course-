# ASSIGNMENT 3:
# Module 4: Functions & Modules in Python 
# Task 1: Calculate Factorial Using a Function 


# Problem Statement: Write a Python program that:
# 1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
# 2.   Returns the calculated factorial.
# 3.   Calls the function with a sample number and prints the output.


# n = int(input("Enter the number here: "))

# def findFactorial(a):
#     for i in range(1,a):
#       a = a * i
#     print(a)

# findFactorial(n)



# Task 2: Using the Math Module for Calculations
 
# Problem Statement: Write a Python program that:
# 1.   Asks the user for a number as input.
# 2.   Uses the math module to calculate the:
# o   Square root of the number
# o   Natural logarithm (log base e) of the number
# o   Sine of the number (in radians)
# 3.   Displays the calculated results.

import math
n = int(input("Enter the number here: "))
print(f"Square root {math.sqrt(n)}")
print(f"log {math.log(n)}")
print(f"Sine {math.sin(n)}")
