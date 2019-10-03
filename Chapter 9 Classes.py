from collections import OrderedDict

class Dog():
	""" Description of the class"""
	def __init__(self, name, age): 
		self.name = name #any variable with the predix self is available to every method in the class
		self.age = age
		self.gender = "male"

	def sit(self):
		"""simulate a puppy sitting"""
		print(self.name.title() + " is now sitting.")

	def get_gender(self):
		print(self.name.title() + "'s gender is " + self.gender)

my_dog = Dog("Buddy", 13)
my_dog.sit()
my_dog.get_gender()

class SamoyedDog(Dog): #as you create a child class, the parent class must be part of the current file and must appear before the child class in the file

	def __init__(self, name, age):
		super().__init__(name, age)
		self.fuzziness = "high"

	def get_fuziness(self):
		print(self.name + " has a " + self.fuzziness + " fuziness level.")

my_samoyed_dog = SamoyedDog("Buddy the Bear", 13)
my_samoyed_dog.sit()
my_samoyed_dog.get_fuziness()

fav_lang = OrderedDict()

fav_lang['Mike'] = "English"
fav_lang['Katie'] = "Chinese"

for name, language in fav_lang.items():
	print(name.title() + "'s fav language is " + language.title())