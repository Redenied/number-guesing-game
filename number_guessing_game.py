#!/usr/bin/env python3

import random

# TODO
# Initial print
# Split into functions

lower = int(input("Lower range: "))
upper = int(input("Upper range: "))

number = random.randint(lower, upper)
answer = False
guess = 0


while not answer:
	guess = int(input("Input your guess: "))
	if guess == number:
		answer = True
	else:
		print("Wrong number, try again.")

print(f"Congratulations! You guessed the number {number}. You won.")
