import random
import sys

''' 
1. allow user to choose whether they want to have duplicates or not
'''

'''
2. if yes: 
	randomly generate a str of R, G, B, Y with out duplicates
   else: 
	randomly generated str could have duplicates, but NOT necessarily must have duplicates
'''

''' 
3. while user input answer does not equal shuffled elements: 
		keep prompting user for input
		keep printing round results
		keep updating remaining rounds 
'''

'''
4. result of game: 
	user won: 
		inform user
		ask user if they would like to play another round
	user ran out of rounds:
		inform user
		ask user if they would like to play another round
'''

default_max_rounds = 10
elements = "RGBY"

def new_round():
	user_new_round = input("Would you like another round?\nAnswer 'y' or 'n'.")
	if user_new_round.upper() == "Y":
		start_round(default_max_rounds)
	elif user_new_round.upper() == "N":
		sys.exit()
	else: 
		print("You have not entered a valid response.")
		return new_round()

def enter_input():
	# enter_input() checks the validity of user's guess
	user_input = input("Please enter your guess. Letter sequencing matters. \nYou may enter 'q' at any time to end the game. Your guess: ")
	if user_input.upper() == "Q":
		sys.exit()
		# Add another check to make sure users type in only RGBY and no other letters.
	if len(user_input) == 4: 
		return user_input
	else:	
		print("You have not entered a valid input, valid inputs consist of 4 letter. Please enter again.")
		return enter_input()

def duplicate():
	# duplicate(): 1. asks if user want to have duplicate color 2. generate the answer key based on user selection
	duplication = input("Would you like to have duplicate colors?\n Answer with 'y' or 'n'. Your answer: ")
	if duplication.upper() == "Y": 
		return ''.join(random.choices(elements, k=len(elements)))
	elif duplication.upper() == "N":
		return ''.join(random.sample(elements, len(elements)))
	else: 
		print("You have not entered a valid response")
		return duplicate()

def start_round(max_rounds):
	shuffled_elements = duplicate()
	rounds = 0
	flag = True
	while rounds < max_rounds: 
		right_place = 0
		wrong_place = 0
		user_inputs = enter_input()
		for index in range(len(shuffled_elements)): 
			if user_inputs[index].upper() == shuffled_elements[index]: 
				right_place += 1
			else: 
				wrong_place += 1
		if user_inputs.upper() == shuffled_elements: 
			flag = False
			print("You won")
			new_round()
		else: 
			print("You have " + str(right_place) + "color in the right place and " + str(wrong_place) + " color in the wrong place")
		rounds += 1
		print("You have " + str(max_rounds - rounds) + " rounds left") 
	if flag: 
		print("You have ran out of rounds. \n The correct answer is " + shuffled_elements)
		new_round()

start_round(default_max_rounds)
