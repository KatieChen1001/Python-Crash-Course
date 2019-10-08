#5.3 Alien Color 1 
alien_color = "red"
if alien_color == "green": 
	print("You have earned 5 points")

#5.4 Alien Color 2 
if alien_color == "green": 
	print("You have earned 5 points for shooting the alien")
else:
	print("You just earned 10 points")
	
#5.5 Alien color 3 if-elif-else chain 
if alien_color == "green": 
	print("You have earned 5 points for shooting the alien")
elif alien_color == "yellow":
	print("You just earned 10 points")
elif alien_color == "red":
	print("you have earned 15 points")
	
#5.8 Hello Admin
usernames = ["mike", "katie", "qiyu", "jamie", "admin" ] 
if usernames:
	for username in usernames: 
		if username == "admin": 
			print("Hello " + username.title() + ", you are special")
		else:
			print("Hello " + username.title())

#5.10 Checking Usernames
current_usernames = ["mike", "katie", "qiyu", "jamie", "rayan", "rakshak"]
new_usernames = ["paul", "MJ", "John", "Judy", "Jamie"]
for new_username in new_usernames:
	if new_username.lower() in current_usernames:
		print(new_username + ", you need a new username") 
	else:
		print(new_username + " is available")
		


