import os
import csv
import xlwt 
from xlwt import Workbook 

path='D:\TeradataUsageAnalysis'
wb = Workbook()
sheet1 = wb.add_sheet('DataSheet') 
rowHeader =0
colHeader=-1
row=-1
listHeader=[]
for csvFileNames in os.listdir(path):
	print("############################")
	if csvFileNames.endswith('.csv'):
		data = open(path+'\\'+csvFileNames,encoding="utf-8-sig")
		count =0
		listValues =[]
		for line in data:
			count=count+1
			if count ==1:
				mapData = dict()
				mapValue=[]
				headerCols= csvFileNames.split('.')
				mapData['Name'] = headerCols[0]
				listHeader.append(str(headerCols[0]).strip())
				#print(rowHeader,colHeader)
				#sheet1.write(colHeader,rowHeader,mapData['Name'])
				colValues= str(line.strip()).split(',')
				cols = 1
				for colValue in colValues:
					listValues.append(colValue)
					print(row,cols,colValue)
					sheet1.write(cols,row,colValue)
					cols=cols+1
				mapData['Columns'] = colValues
				listValues.append(mapData)
	colHeader=colHeader+1
	row=row+1
	print("############################")	
print(listHeader)
wb.save('xlwt example.xls')	
	