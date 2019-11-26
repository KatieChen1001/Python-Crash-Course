import random

''' 
1. allow user to choose whether they want to have duplicates or not
'''

elements = "RGBY"
duplication = input("Would you like to have duplicate colors?\n Answer with 'y' or 'n'. ")

'''
2. if yes: 
	randomly generate a str of R, G, B, Y with out duplicates
   else: 
	randomly generated str could have duplicates, but NOT necessarily must have duplicates
'''

if duplication.upper() == "Y": 
	shuffled_elements = ''.join(random.choices(elements, k=len(elements)))
elif duplication.upper() == "N":
	shuffled_elements = ''.join(random.sample(elements, len(elements)))
else: 
	print("You have not entered a valid response")

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

def new_round():
	new_round = input("Would you like another round?\nAnswer 'y' or 'n'. ")
	if new_round.upper() == "Y":
		start_round(default_max_rounds)
	elif new_round.upper() == "N":
		sys.exit()
	else: 
		print("You have not entered a valid response. ")
		return new_round()

def start_round(max_rounds):
	rounds = 0
	flag = True
	while rounds < max_rounds: 
		right_place = 0
		wrong_place = 0
		user_inputs = input("\nLetter sequencing matters: ")
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
		print("You have ran out of rounds")
		new_round()

print(shuffled_elements)
start_round(default_max_rounds)
