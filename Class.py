


class Pokemon:
	'This class contains info about pokemons'
	def __init__(self, name, cp, p_type):
		self.pokemon_name = name
		self.pokemon_cp = cp
		self.pokemon_type = p_type

	def DisplayInfo():
		print "My Pokemon %s is a %s type with CP %d" %(Pokemon.pokemon_name, Pokemon.pokemon_type, Pokemon.pokemon_cp)

squirtle = Pokemon('Squirtle', 40, 'Water')
squirtle.DisplayInfo()