#!/usr/bin/env python3

import random

# TODO
# Initial print
# Split into functions

def guessing(number):
	# Initialize loop variables
	answer = False
	guess = 0

	# Keep trying as long as answer is not True
	while True:
		try:
			guess = int(input("Input your guess: "))
			if guess == number:
				answer = True
				break
			elif guess > number:
				print("Too high!")
			elif  guess < number:
				print("Too low!")
		except ValueError:
			print("Please enter a valid number.")
	return answer

def main():
	# Initial print
	print("Welcome to the Number Guessing game!\nPlease input the number range for this game.")

	# Get range provided by the user
	lower = int(input("Lower range: "))
	upper = int(input("Upper range: "))

	# Get random number within given range
	number = random.randint(lower, upper)

	# Print success message when guessed right
	if guessing(number) == True:
		print(f"Congratulations! You guessed the number {number}. You won.")

	# Play again if user answers yes
	play_again = input("Want to play again?(Y/N) ").lower()
	if play_again == "y":
		main()

main()
