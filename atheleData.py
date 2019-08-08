

def readingValues(values):
	arrData=[]
	finData=[]
	for data in values:
		if isinstance(data,list):
			readingValues(data)
		else:
			varData = data.strip().split(',')
			for var in varData:
				finData.append(var)
	return finData

def sanitize(values):
	cleanData=[]
	for value in values:
		cleanData.append(value.replace('-',':').replace('.',':'))
	return cleanData

def remove_duplicates(values):
	ultimateValue=[]
	for value in values:
		if value not in ultimateValue:
			ultimateValue.append(value)
	return ultimateValue[0:3]

try:
	dataOfJulie = open('julie.txt')
	dataOfJames = open('james.txt')
	dataOfSarah = open('sarah.txt')
	dataOfMikey = open('mikey.txt')



	dataJulie = readingValues(dataOfJulie)
	dataJames = readingValues(dataOfJames)
	dataSarah = readingValues(dataOfSarah)
	dataMikey = readingValues(dataOfMikey)

	julie=sorted(sanitize(dataJulie))
	james=sorted(sanitize(dataJames))
	sarah=sorted(sanitize(dataSarah))
	mikey=sorted(sanitize(dataMikey))

	print(remove_duplicates(julie))
	print(remove_duplicates(james))
	print(remove_duplicates(sarah))
	print(remove_duplicates(mikey))


except IOError as ieerr:
	print("IOError"+ierr)
except Error as err:
	print("Error"+err)
finally:
	if 'dataOfJulie' in locals():
		dataOfJulie.close()
	if 'dataOfJames' in locals():
		dataOfJames.close()
	if 'dataOfSarah' in locals():
		dataOfSarah.close()
	if 'dataOfMikey' in locals():
		dataOfMikey.close()

