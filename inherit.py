class NamedList(list):
	def __init__(self,a_name):
		list.__init__([])
		self.name = a_name


jibanendu= NamedList('Jibanendu')
print(type(jibanendu))

print(dir(jibanendu))
