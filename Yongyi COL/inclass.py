#Katie Chen 

#description: isLeapYear determines if a year is a run nian or not

def isLeapYear(my_year):
	if len(my_year) != 4: 
		print("You have not entered a valid year")
		user_input = input("Enter a year: ")
		isLeapYear(user_input)
	else: 
		if int(my_year) % 4 == 0 and int(my_year) % 100 != 0:
			print("run nian")
		elif int(my_year) % 400 == 0:
			print ("shi ji run nian")
		else: 
			print ("you have entered a not important year" )
			user_input = input("Enter a year: ")
			isLeapYear(user_input)
		

#descrption: isPrime determines if a number is prime
import math
def isPrime(my_number):
	if int(my_number) == 0 or int(my_number) == 1:
		print(my_number + " is not a prime number")
		return(isPrime(input("Enter a number and I will tell you if it is a prime number: ")))
	elif int(my_number) == 2:
		print("2 is a prime number")
	else: 
		root = math.floor(math.sqrt(int(my_number)))
		flag = True
		for index in range(2, root+1):
			if int(my_number) % index == 0:
				flag = False 
				print("Not a prime num")
				return(isPrime(input("Enter a number and I will tell you if it is a prime number: ")))
	if flag: 
		print(my_number + " is a prime number")

user_input = input("Enter a year: ")
isLeapYear(user_input)
user_input = input("Enter a number and I will tell you if it is a prime number: ")
isPrime(user_input)


