#!/usr/bin/python3
import random

# Generate a random integer between -10000 and 10000
number = random.randint(-10000, 10000)

# Extract the last digit of the number
last_digit = abs(number) % 10
# Output the specified format
if number < 0:
    last_digit *= -1

# Check the conditions and print the appropriate message
if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
