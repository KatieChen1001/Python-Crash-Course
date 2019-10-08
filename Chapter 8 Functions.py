#8.3 T shirt 

def make_shirt(size = "large", text ="I Love Python"):
	"""defines the text and size of a t shirt"""
	print("The size of the T shirt is " + size)
	print("The T shirt says: " + text)
message = ""
while message.upper() != "N": 
	my_size = input("What is your T shirt size? ")
	my_text = input("What would you like to write on the T shirt? ")
	make_shirt(size=my_size, text=my_text)
	message = input("Would you like to make another shirt? Y/N")

	
