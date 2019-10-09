#猜丁壳
#导入库
from random import randint
#游戏介绍
def introduce():
    print("这是一个石头剪刀布的游戏")
    print("请点击开始进行游戏")
    print("每赢一局分数加一,采取五局三胜制")
#获取输入
def got():
    f = True
    print("请输入“石头”或“剪刀”或“布”")
    while f:
        x = 0
        n = str(input())
        if n in ["石头"]:
            x = 1
            f = False
        elif n in ["剪刀"]:
            x = 2
            f = False
        elif n in ["布"]:
            x = 3
            f = False
        else:
            print("您的输入不符合规范")
            print("请再输一遍")
            f = True
    return x
#产生随机手势
def create():
    y = randint(1,3)
    if y == 1:
        print("石头")
    elif y == 2:
        print("剪刀")
    else:
        print("布")
    return y
#比较大小
def compare(x,y,a,b):
    if x == y:
        print("你们打平了".center(9,"-"))
    elif x == 1 and y == 3:
        print("你输了".center(10,"-"))
    elif x < y :
        print("你赢了".center(10,"-"))
        a += 1
    elif x == 3 and y == 1:
        print("你赢了".center(10,"-"))
        a += 1
    else:
        b += 1
        print("你输了".center(10,"-"))
    return a,b
#主函数
def main():
    a,b =0,0
    introduce()
    for i in range(5):
        x = got()
        y = create()
        a ,b = compare(x,y,a,b)
        if a == 3 or b == 3:
            break
    print("你的最终得分为:{}\n电脑的最终得分为:{}".format(a,b))
    if a > b:
        print("你获得了最终的胜利")
    elif a < b:
        print("你输掉了这场游戏")
    else:
        print("你们最终打平了")
    print("游戏结束".center(10,"#"))
#递归
def again():
    main()
    t = 1
    print("你想要再玩一遍吗？")
    j = str(input())
    if j in ["不想"]:
        t = 0
    else:
        t = 1
    if t == 1:
        again()
    else:
        return
again()