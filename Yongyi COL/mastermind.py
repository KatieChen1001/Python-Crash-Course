
import random

elements = "RGBY"
shuffled_elements = ''.join(random.sample(elements, len(elements)))

''' 
1. randonly generate a str of R, G, B, Y
2. store str in a variable
'''

''' 
3. while user input answer does not equal shuffled elements: 
		keep prompting user for input
		keep printing round results
'''
#print(shuffled_elements)

rounds = 0
max_rounds = 10

while rounds <= max_rounds: 
	right_place = 0
	wrong_place = 0
	user_inputs = input("Letter sequencing matters: ")
	for index in range(len(shuffled_elements)): 
		if user_inputs[index].upper() == shuffled_elements[index]: 
			'''
			print("right place user input: " + user_inputs[index])
			print("right place answer: " + shuffled_elements[index])
			'''
			right_place += 1
		else: 
			'''
			print("wrong place user input: " + user_inputs[index])
			print("wrong place answer: " + shuffled_elements[index])
			'''
			wrong_place += 1
	if user_inputs.upper() == shuffled_elements: 
		print("You won")
		break
	else: 
		print("You have " + str(right_place) + "color in the right place and " + str(wrong_place) + " color in the wrong place")
	rounds += 1
	
print("You have ran out of rounds")
