class AthleteList(list):
	def __init__(self,a_name,a_dob=None,a_times=[]):
		list.__init__([])
		self.name=a_name
		self.dob=a_dob
		self.extend(a_times)

	def sanitize(timestring):
		if '-' in timestring:
			splitter='-'
		elif ':' in timestring:
			splitter=':'
		else:
			return timestring
		(mins,sec) =timestring.split(splitter)
		return mins+'.'+sec
		
	def top3_self(self):
		return(sorted(set([AthleteList.sanitize(t)for t in self]))[0:3])

def get_coach_data(fileName):
	try:
		with open(fileName) as f:
			data = f.readline()
			temp =data.strip().split(',')
			return(AthleteList(temp.pop(0),temp.pop(0),temp))
	except IOError as ioerror:
		print("Error:"+str(ioerror))
		return(None)

sarah = get_coach_data('sarah2.txt')
print(sarah.name)
print(sarah.top3_self())