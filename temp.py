temp = input("请输入温度")
if temp[-1] in ['f', 'F']:
    C = (eval(temp[0:-1]) - 32)/1.8
    print('转换后的温度是{:.2f}C'.format(C))
elif temp[-1] in ['c', 'C']:
    F = 1.8*eval(temp[0:-1]) + 32
    print('转换后的温度是{:.2f}F'.format(F))
else:
    print("输入错误")