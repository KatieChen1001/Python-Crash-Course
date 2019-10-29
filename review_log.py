
taglist = {}       

typing = True

while typing: 
	new_tag_name = input("New Tag Name = ")
	
	if new_tag_name == 'q':
		typing = False
		print("existing program")
		break
	
	if new_tag_name in taglist:
		taglist[new_tag_name] += 1 
	else: 
		taglist[new_tag_name] = 1
	print(taglist)
	
		
