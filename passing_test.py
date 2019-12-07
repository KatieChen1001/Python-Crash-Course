import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
	"""TEsts for name_function.py"""
	def test_first_last_name(self):
		"""DO names like Janis Joplin work?"""
		formatted_name = get_formatted_name('janos', 'jk')
		self.assertEqual(formatted_name, 'Janos Jk')

unittest.main()