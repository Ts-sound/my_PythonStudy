# -- coding: utf-8 --
import re

'''
将32位补码数据转换为int类型数据

'''


def byte32ToInt(byte32):
    if(byte32 & 0x80000000 == 0):
        r = byte32
    else:
        byte32 = byte32 ^ 0xFFFFFFFF
        byte32 = byte32 + 1
        r = -byte32
    return r

'''
bytes:字节数组
return 组合后的值(高位在前)

'''


def combinationBytes(a_bytes=[]):
    lenth = len(a_bytes)
    result = 0
    for i in range(0, lenth):
        result += a_bytes[i] << (8 * (lenth - 1 - i))
    return result


'''    end    '''

'''
dataAnalysis

'''


def informationDataAnalysis(matrix=[[]]):
    result_Matrix = [[]]
    
    result_Matrix[0] = ['car.direction', 'car.speed', 'car.input', 'car.warningcode', 'car.errorcode', 'car.y', 'car.theta']
    print(result_Matrix)
    
    for raw in range(0, len(matrix)):
        temp = [0, 0, 0, 0, 0, 0, 0]
        temp[0] = matrix[raw][7]
        temp[1] = matrix[raw][8]
        temp[2] = combinationBytes(matrix[raw][13:17])
        temp[3] = matrix[raw][25]
        temp[4] = matrix[raw][26]
        temp[5] = byte32ToInt(combinationBytes(matrix[raw][39:43]))/1000
        temp[6] = byte32ToInt(combinationBytes(matrix[raw][43:47]))/1000
        
        result_Matrix.append(temp)
        
    return result_Matrix
    
