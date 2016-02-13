class Collectible(object):
	''' There will be some collectibles.

	Ones that give 50, 100, 500, 1000 points.
	Those for 50 and 100 points will also prevent pakias
	from coming for a while.

	One to clone pappu, it'll kill all forks, branches, and pakias.
	'''
	def __init__(self):
		self.count = 2
		self.types = ['point', 'clone']
		self.sub_types = {
			'point': [50, 100, 500, 1000]
		}

	def create(self):
		pass

	def draw(self):
		pass