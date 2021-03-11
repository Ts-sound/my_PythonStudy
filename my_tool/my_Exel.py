import xlwt

def dataWriteToExel(matrix=[[]], fileName='null.xls'):
  '''
        向Excel中写入数据（矩阵）

  '''
  xl = xlwt.Workbook(encoding='utf-8');

  sheet1 = xl.add_sheet('data1')
 
  # write matrix data 
  for row in range(0, len(matrix)):
    for colunm in range(0, len(matrix[row])):
      sheet1.write(row, colunm, matrix[row][colunm])
    
  xl.save(fileName)

if __name__ == '__main__':
  matrix_1 = [['she',2,3],[4,5,6],[7,8,10]]
  dataWriteToExel(matrix_1,r'G:\\Test\\1.xls')   #绝对路径
#  dataWriteToExel(matrix_1,'1.xls')   #相对路径
else:
    print ('')
