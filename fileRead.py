import os


dirCheck = os.getcwd();
print('Directory:',dirCheck)
if dirCheck == 'C:\\Users\\52033082\\Desktop\\Nester':
	'''print('success')'''
	data = open('data.txt')
	for line in data:
		if not line.find(':')== -1:
			try:
				(role,dataValue) = line.split(':',1)
				print(role,end='')
				print('said',end='')
				print(dataValue)
			except ValueError:
				   pass
	data.close()
else:
    print('Error')
