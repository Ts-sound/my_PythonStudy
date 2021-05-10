# -- coding: utf-8 --
from mytool.RawDataFilter import rawDataFilter, combinationBytes
from mytool.my_pltDraw import drawSinglePicture
from mytool.myWriteExel import dataWriteToExel
from mytool.my_dataAnalysis import informationDataAnalysis

# openfile savefile

DATA = open("2021-05-10-12OverLook.txt", "rb").read().decode('utf-8')
matrix = []
FileName = '2021-05-10-12OverLook.xls'

'''
data filter
'''
matrix = rawDataFilter(DATA)
print(matrix)
# print(len(matrix))

'''
data analysis
'''
matrix = informationDataAnalysis(matrix)

'''
data write to file
'''
dataWriteToExel(matrix, FileName);

x, y = [], [] 

for i in range(1, len(matrix)):
    x.append(i)
    y.append(matrix[i][9])

drawSinglePicture(x, y, 't','m',matrix[0][9])

