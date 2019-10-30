import json

data = {}

try: 
	data_file = open('taglist.json', 'r+')
	data = json.load(data_file)
except IOError as e: 
	print(e)
	print("something went wrong")
	
	
typing = True

while typing: 
	input_tag_name = input("New Tag Name = ")
	new_tag_name = input_tag_name.lower()
	
	if new_tag_name == 'q':
		typing = False
		json.dump(data, data_file, indent=4, sort_keys=True)
		data_file.close()
		print("closing file and existing program...")
		break

	if new_tag_name in data:
		data[new_tag_name] += 1
		print(data)
	else: 
		data[new_tag_name] = 1
		print(data)
	
	
