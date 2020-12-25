
def byte32ToInt(byte32):
  '''
      将32位补码数据转换为int类型数据
  '''
  if(byte32 & 0x80000000 == 0):
      r = byte32
  else:
      byte32 = byte32 ^ 0xFFFFFFFF
      byte32 = byte32 + 1
      r = -byte32
  return r

def hex_to_int(hex_arr8 = "ffffffff"):
  '''
      将hex数据(8位 ，如：A0B00100)转换为int类型数据
  '''
  r = byte32ToInt(int(hex_arr8,16))  #16表示该字符串为16进制（hex）数据
  
  return r


if __name__ == '__main__':
  a = "ffffffff"
  print(hex_to_int(a))
else:
    print ('')