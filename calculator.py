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
def get_user_input():
	while True:
		valid_operators = ["+", "-", "*", "/", "square", "cube", "power", "%"]	
		print("Enter an operator followed by 1-2 numbers.")
		user_input = input("> ").split()
		if user_input[0].startswith("q"):
			return(False)
		if user_input[0] in valid_operators:
			return(user_input)
		else:
			print("Enter a valid operator.")

while True:
	math_list = get_user_input()
	if math_list is False:
		break

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

	if math_list[0] == "pow":
		print(power(float(math_list[1]),float(math_list[2])))

	if math_list[0] == "%":
		print(mod(float(math_list[1]),float(math_list[2])))	

