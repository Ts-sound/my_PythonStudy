# -- coding: utf-8 --
#import xlrd
import xlwt

data = []

for line in open("16data.txt","r"): 
    data.append(line)
    
print(data)
print(len(data))

char1  = [];
 
for a in data:
    y = bytearray.fromhex(a)
    z = list(y)
    print(z)

#向Excel表中写数据
xl = xlwt.Workbook(encoding = 'utf-8');

sheet1 = xl.add_sheet('data1')
print(sheet1)

i = 0
del a
for a in z:
    i += 1;
    sheet1.write(i,1,1)

xl.save("data.xls")


