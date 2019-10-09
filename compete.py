from random import random
from time import perf_counter
def introduce():
    print("这是一个模拟体育竞技的程序")
    print("接下来需要你输入两球员的能力值，和你想要模拟的场次")
def got():
    a = float(input("A选手的能力值:"))
    b = float(input("B选手的能力值:"))
    n = int(input("模拟场次:"))
    imitate(n,a,b)
def imitate(n,a,b):
    a1,b1,p = 0,0,0
    for i in range(n):
        a1,b1,p = onetime(a,b,p,a1,b1)
    a2 = a1/n
    b2 = b1/n
    p1 = p/n
    sum(a1,a2,b1,b2,p,p1)
def onetime(a,b,p,a1,b1):
    x = random()
    y = random()
    dot1 = 0
    dot2 = 0
    if x < a:
        dot1 += 1
    elif x == a:
        dot1 += 0
    else:
        dot1 -= 1
    if y < b:
        dot2 += 1
    elif y == b:
        dot2 += 0
    else:
        dot2 -= 1
    if dot1 > dot2:
        a1 += 1
    elif dot1 < dot2:
        b1 += 1
    else:
        p += 1
    return a1,b1,p
def sum(a1,a2,b1,b2,p,p1):
    print("A选手的胜利场次为:{},他的胜率为:{:.2f}%\n\
B选手的胜利场次为:{},他的胜率为:{:.2f}%\n\
他们平局的场次为:{},占总场数:{:.2f}%".format(a1,a2*100,b1,b2*100,p,p1*100))
def main():
    introduce()
    got()
w = perf_counter()
main()
print("该程序总耗时{:.3f}s".format(perf_counter()-w))