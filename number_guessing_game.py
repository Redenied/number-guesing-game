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
	while not answer:
		guess = int(input("Input your guess: "))
		if guess == number:
			answer = True
		elif guess > number:
			print("Wrong number, try again. Try a smaller number.")
		elif guess < number:
			print("Wrong number, try again. Try a greater number.")

	return answer

def main():
	# Get range provided by the user
	lower = int(input("Lower range: "))
	upper = int(input("Upper range: "))

	# Get random number within given range
	numer = random.randint(lower, upper)

	# Print success message when guessed right
	if guessing(number) == True:
		print(f"Congratulations! You guessed the number {number}. You won.")

	# Play again if user answers yes
	play_again = input("Want to play again?(Y/N) ").lower()
	if play_again == "y":
		main()

main()
