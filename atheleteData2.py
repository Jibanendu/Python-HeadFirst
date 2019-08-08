def santize(timestring):
	if '-' in timestring:
		splitter='-'
	elif ':' in timestring:
		splitter=':'
	else:
		return timestring
	(mins,sec) =timestring.split(splitter)
	return mins+'.'+sec

def get_coach_data(fileName):
	try:
		with open(fileName) as f:
			data = f.readline()
			return(data.strip().split(','))
	except IOError as ioerror:
		print("Error:"+str(ioerror))
		return(None)

sarah = get_coach_data('sarah2.txt')
sarahData ={}
sarahData['Name']=sarah.pop(0)
sarahData['DOB']=sarah.pop(0)
sarahData['Times']=sarah

value = str(sorted(set([santize(t) for t in sarahData['Times']]))[0:3])
print(sarahData['Name']+"'s fastest times are:"+value)