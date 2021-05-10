import re

'''
将32位补码数据转换为int类型数据

'''
def byte32ToInt(byte32):
    if(byte32&0x80000000 == 0):
        r = byte32
    else:
        byte32 = byte32^0xFFFFFFFF
        byte32 = byte32 + 1
        r = -byte32
    return r
'''
data:原始数据
return 过滤后的数组(二维数组，每一行代表一组数据)

'''
def rawDataFilter(data):
    temp = []
    array = []
    
    #利用正则过滤出需要的字符串
    it = re.finditer(r"A0B001\w{98}",data)
    for match in it: 
        temp.append(match.group())
    
    #hex数据转成byte类型    
    for line in temp:
        a = list(bytearray.fromhex(line))
        array.append(a)

    return array

'''
bytes:字节数组
return 组合后的值(高位在前)

'''
def combinationBytes(a_bytes = []):
    lenth = len(a_bytes)
    result = 0
    for i in range(0,lenth):
        result += a_bytes[i] << (8 * (lenth - 1 - i))
    return result
'''    end    '''

 
if __name__ == '__main__':

    #打开原始数据文件
    DATA = open("OverLook.txt","rb").read().decode('utf-8')
    print(DATA)
    result_array = []
    result_array = rawDataFilter(DATA)
 
    print(result_array)
    print(result_array[0][1])
else:
    print ('')
