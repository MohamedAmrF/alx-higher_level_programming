#!/usr/bin/python3
number = 11
digit = number % 10
print(f"Last digit of {number} is {digit}", end=' ')
if digit > 5:
	print(f"greater than 5")
elif digit == 0:
	print(f"and is 0")
else:
	print(f"and is less than 6 and not 0")
