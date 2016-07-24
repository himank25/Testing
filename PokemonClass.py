


class Pokemon:
	'This class contains info about pokemons'
	def __init__(self, name, cp, p_type):
		self.pokemon_name = name
		self.pokemon_cp = cp
		self.pokemon_type = p_type
		self.__foo = 'Private Member'

	def DisplayInfo(self):
		print "My Pokemon %s is a %s type with CP %d" %(self.pokemon_name, self.pokemon_type, self.pokemon_cp)

squirtle = Pokemon('Squirtle', 40, 'Water')
squirtle.DisplayInfo()
print squirtle.__foo