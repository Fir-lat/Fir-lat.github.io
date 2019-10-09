import turtle as t
from random import random
#创建画布
t.title("Auto Draw Lines")
t.setup(1000,800)
t.pensize(3)
t.pencolor("green")
#读取文件
d = []
txt = open("C:/Users/Fir's/Cprime/f.txt","rt")
for line in txt:
    line = line.replace("\n","")
    d.append(list(map(eval,line.split(","))))
txt.close()
#开始绘制
for i in range(len(d)):
    t.fillcolor(random(),random(),random())
    t.begin_fill()
    t.pencolor(d[i][3],d[i][4],d[i][5])
    t.circle(d[i][0],30)
    if d[i][1]:
        t.right(d[i][2])
    else:
        t.left(d[i][2])
    t.end_fill()
t.hideturtle()
t.done()