import re

varString = ['Call Center - Houston Silverscript Outbound – 666387','Call Center1 - Houston Silverscript Outbound1 - 666388']

for values in varString:
	arr=re.split('–|-',values)
	print(arr[0])
	print(arr[1])
	print(arr[2])
