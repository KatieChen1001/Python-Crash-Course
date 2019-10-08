#print the square of 1 - 10
squares = []
for value in range(1,11):
	squares.append(value **2)
print(squares)

#list comprehensions
squares = [ value**2 for value in range (1,11)]
print(squares)

#4.3 counting to twenty 
count_to_twenty = [value for value in range(1,21)]
print(count_to_twenty)

count_to_million = [value for value in range(1,10000001)] #4.4 count to million 
#print(count_to_million)

#print(sum(count_to_million)) #4.5 summing a million

odd_numbers = list(range(1,21,2)) #4.6 print odd numbers from 1-20
print(odd_numbers)

multiples_of_3 = [value*3 for value in range(3, 31)]
print(multiples_of_3) #4.7 print multiples of 3 from 3 to 30

cubes = [value**3 for value in range(1,11)]
print(cubes) #4.8 cubes

print("\n")

modern_artists = ["Dali", "Picasso", "Andy Warhol", "Miro", "Matissee"]
print("Here are the first three artists:")
for artist in modern_artists[:3]:
	print(artist)
comtemporary_artists = modern_artists[:]
print(comtemporary_artists)
modern_artists.append("Miro")
comtemporary_artists.append("Jeff Koons")
print("My modern artists are:")
for artist in modern_artists: 
	print(artist)
print("My comtemporary artists are:")
for artist in comtemporary_artists:
	print(artist)




