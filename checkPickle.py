import pickle
import nester

new_man=[]

try:
	with open('man_data.txt','rb') as restoredData:
		new_man=pickle.load(restoredData)
	nester.print_values(new_man)
except IOError as err:
	print("File Error:"+err)
except pickle.PickleError as perr:
	print("PickleError:"+perr)