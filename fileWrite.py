import os
import pickle

man=[]
am=[]
man_data = open("man_data.txt",'wb')
anotherman_data = open("anotherman_data.txt",'wb')
dirCheck = os.getcwd();
if dirCheck == 'C:\\Users\\52033082\\Desktop\\Nester':
	try:
		data=open("data.txt")
		for line in data:
			if not line.find(':')== -1:
				try:
					(role,dataValue) = line.split(':',1)
					#print(role,dataValue)
					dataValue=dataValue.strip()
					if role=='Man':
						man.append(dataValue)
					elif role=='AM':
						am.append(dataValue)
				except ValueError:
					pass
		#print(man,file=man_data)
		#print(am,file=anotherman_data)
		pickle.dump(man,man_data)
		pickle.dump(am,anotherman_data)
	except IOError as err:
		print('File is Missing'+err)
	except pickle.PickleError as perr:
		print('PickleError'+perr)
	finally:
		data.close()
		man_data.close()
		anotherman_data.close()