
taglist = []       

typing = True

while typing: 
	new_tag_name = input("New Tag Name = ")
	
	if new_tag_name == 'q':
		typing = False
		print("existing program")
		break

	if not taglist: 
		print("empaty array")
		new_tag = {}
		new_tag['tagName'] = new_tag_name
		new_tag['counter'] = 1
		taglist.append(new_tag)
		print(taglist)
	
	else: 
		
		for index in range(len(taglist)):
			for key in taglist[index]: 
				print(taglist[index][key])
		
		# for tags in taglist: 
			# if tags['tagName'] == new_tag_name: 
				# print("this tag already exists")
				# count = int(tags['counter'])
				# tags['counter'] = count + 1
				# print(taglist)
			# else: 
				# print("got a new tag")
				# taglist.append({'tagName': new_tag_name, 'counter': 1})
				# break
	
		
