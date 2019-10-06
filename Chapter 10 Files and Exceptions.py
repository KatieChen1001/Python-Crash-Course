import json
# When desired file and current program is under the same directory
with open('pi_digits.txt') as file_object: 
	#contents = file_object.read()
	lines = file_object.readlines()
	#print(contents)

# first open("name of the file you want to access") the file to access 
# Python stores the file as an object in file_object 
pi_string = ""
for line in lines: 
	pi_string += line.strip()

print(pi_string)
print(len(pi_string))

numbers = [3,2 ,4,2,3,21,1 ,12,12,2]
filename="numbers.json"
with open(filename, 'w') as file_object:
	json.dump(numbers, file_object)