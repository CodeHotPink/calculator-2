"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


"""
Keep looping until "q"
Get input from user
	check conditions to know which math function to run
	call the math function
"""

user_input = input("")
math_list = user_input.split(" ")
if math_list[0] == "+":
	print(add(float(math_list[1]),float(math_list[2])))

if math_list[0] == "-":
	print(subtract(float(math_list[1]),float(math_list[2])))

if math_list[0] == "*":
	print(multiply(float(math_list[1]),float(math_list[2])))	

if math_list[0] == "/":
	print(divide(float(math_list[1]),float(math_list[2])))	

if math_list[0] == "square":
	print(square(float(math_list[1])))

if math_list[0] == "cube":
	print(cube(float(math_list[1])))

