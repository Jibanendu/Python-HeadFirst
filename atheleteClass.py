class Athlete:
	def __init__(self,a_name,a_dob=None,a_time=[]):
		self.name=a_name
		self.dob=a_dob
		self.time=a_time

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
		return(sorted(set([Athlete.sanitize(t)for t in self.time]))[0:3])

	def add_time(self,time_value):
		self.time.append(time_value)

	def add_times(self,list_of_times):
		self.time.extend(list_of_times)


def get_coach_data(fileName):
	try:
		with open(fileName) as f:
			data = f.readline()
			temp =data.strip().split(',')
			return(Athlete(temp.pop(0),temp.pop(0),temp))
	except IOError as ioerror:
		print("Error:"+str(ioerror))
		return(None)
	

sarah = get_coach_data('sarah2.txt')
james = get_coach_data('james2.txt')
julie = get_coach_data('julie2.txt')
mikey = get_coach_data('mikey2.txt')

vera = Athlete('Vera')
vera.add_time('1.31')
listTimes =['1.45','4.3']

vera.add_times(listTimes)

print(vera.name+"'s top runs are "+str(vera.top3_self()))

print(sarah.name+"'s top runs are "+str(sarah.top3_self()))
print(james.name+"'s top runs are "+str(james.top3_self()))
print(julie.name+"'s top runs are "+str(julie.top3_self()))
print(mikey.name+"'s top runs are "+str(mikey.top3_self()))