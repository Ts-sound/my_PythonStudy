a = 21047



line = ['准备上电','已上电','使能','故障', #
        '禁止输出电压','快速停止','上电禁止','警告',#
        '内部保留','远程控制','目标位置到','内部限位激活',#
        '脉冲响应','跟随误差','找到电机励磁','原点找到']

# bit0：准备上电
# bit1：已上电
# bit2：使能
# bit3：故障
# bit4：禁止输出电压
# bit5：快速停止
# bit6：上电禁止 bit7：警告
# bit8：内部保留
# bit9：远程控制
# bit10：目标位置到
# bit11：内部限位激活
# bit12：脉冲响应
# bit13：跟随误差/原点错误
# bit14：找到电机励磁
# bit15：原点找到

def get_bit(data, index):
  return (data >> index) & 0x1

for i in range(0,len(line)):
  print(line[i] + str(get_bit(a, i)))

