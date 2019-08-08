import pickle
import AthleteList 

def get_coach_data(fileName):
	try:
		with open(fileName) as f:
			data = f.readline()
			temp =data.strip().split(',')
			value = AthleteList(temp.pop(0),temp.pop(0),temp)
			return(value)
	except IOError as ioerror:
		print("Error:"+str(ioerror))
		return(None)

def put_to_store(files_list):
	all_atheletes={}
	for athList in files_list:
		athData = get_coach_data(athList)
		all_atheletes[athData.name] = athData
	try:
		with open('atheletesPickle','wb') as athPickle:
			pickle.dump('all_atheletes', athPickle)
	except IOError as ioerror:
		print('File Error:'+str(ioerror))
	except PickleError as perror:
		print('Pickle Error'+str(perror))
	return(all_atheletes)

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


def get_from_store():
	all_athletes = {}
	try:
		with open('atheletesPickle','rb') as athReadPickle:
			all_atheletes=pickle.load(athReadPickle)
	except IOError as ioerror:
		print('File Error:'+str(ioerror))
	except PickleError as perror:
		print('Pickle Error'+str(perror))

	return(all_atheletes)

the_files = ['sarah2.txt', 'james2.txt', 'mikey2.txt', 'julie2.txt']
data = put_to_store(the_files)
print(data)