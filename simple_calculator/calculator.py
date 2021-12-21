#!/usr/bin/env python3

__author__ = 'ehsangb180@gmail.com'

'''
	1)Create a simple menu.
	2)How to grab value using input() method.
	3)While loop and asking for continue.
	4)Trace Code.

'''
import os
from termcolor import cprint

os.system('clear')
cprint(f'This is a simple Calculator using python3.8 created by {__author__}', 'green')

while True:
	operation = input('''
Choose Operation:

For:
  * Addition    ==> +
  * Subtraction ==> -
  * Multi       ==> *
  * Division    ==> /
  * Exit        ==>'q'
  : ''')

	if operation == 'q' or operation == 'quit':
		cprint('Have a good time.', 'green', attrs=['blink'])
		break

	elif operation == '+':	
		try:
			number1 = int(input('Enter first number: '))
			number2 = int(input('Enter second number: '))
			cprint(f'Sum: {number1 + number2 }', 'yellow')
			
		except ValueError:
			cprint('You should enter an Integer.', 'red', attrs=['blink'])
			continue
			
		operation = input('continue? y/n: ')
		if operation == 'n':
			cprint('Have a good time.', 'green', attrs=['blink'])	
			break 
		os.system('clear')

	elif operation == "-":
		try:
			number1 = int(input('Enter first number: '))
			number2 = int(input('Enter second number: '))
			cprint(f'Sub: {number1 - number2 }','yellow')
		
		except ValueError:
			cprint('You should enter an Integer.', 'red', attrs=['blink'])
		
		operation = input('continue? y/n: ')
		if operation == 'n':
			cprint('Have a good time.', 'green', attrs=['blink'])			
			break
		os.system('clear')

	elif operation == "*":
		try:
			number1 = int(input('Enter first number: '))
			number2 = int(input('Enter second number: '))
			cprint(f'Mul: {number1 * number2 }','yellow')
		
		except ValueError:
			cprint('You should enter an Integer.', 'red', attrs=['blink'])
		
		operation = input('continue? y/n: ')
		if operation == 'n':
			cprint('Have a good time.', 'green', attrs=['blink'])			
			break
		os.system('clear')

	elif operation == "/":
		try:
			number1 = int(input('Enter first number: '))
			number2 = int(input('Enter second number: '))
			cprint(f'Div: {number1 / number2 }','yellow')
		
		except ValueError:
			cprint('You should enter an Integer.', 'red', attrs=['blink'])
		
		except ZeroDivisionError:
			cprint('Division by zero', 'red', attrs=['blink'])
		
		operation = input('continue? y/n: ')
		if operation == 'n':
			cprint('Have a good time.', 'green', attrs=['blink'])			
			break
		os.system('clear')


	else:
		cprint('Invalid input.', 'red', attrs=['blink'])
