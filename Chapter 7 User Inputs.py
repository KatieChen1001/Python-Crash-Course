prompt = "\nTell me something and I will say it back to you"
prompt += "\nEnter 'quit' to end the program: "
message = ""
while message != "quit": 
	message = input(prompt)
	if message != 'quit':
		print(message)

current_number = 0
while current_number <= 10:
	reminder = current_number%2
	
	if reminder != 0: 
		print(current_number)
	current_number = current_number + 1
