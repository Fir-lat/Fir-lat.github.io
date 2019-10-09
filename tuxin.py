import turtle as t
t.setup(1000,800)
t.pu()
t.fd(-400)
t.goto(-400,300)
t.pd()
t.pensize(5)
t.pencolor("red")
#正方形
for i in range(4):
    t.pencolor("blue")
    t.fd(80)
    t.right(90)
t.pu()
t.goto(-250,300)
t.pd()
#六边形
for i in range(6):
    t.fd(80)
    t.right(60)
t.pu()
t.goto(-300,-100)
t.pd()
#九角心
t.fillcolor("red")
t.begin_fill()
for i in range(9):
    t.fd(150)
    t.left(80)
t.end_fill()
t.pu()
t.goto(200,0)
t.pd()
#十五角形
t.fillcolor("red")
t.begin_fill()
for i in range(15):
    t.fd(100)
    t.left(48)
t.end_fill()
t.pu()
t.goto(0,0)
t.pd()
#大风车
t.fillcolor("red")
t.begin_fill()
for i in range(4):
    t.fd(80)
    t.right(90)
    t.circle(-40,45)
    t.right(90)
    t.fd(80)
    t.right(45)
t.end_fill()
#九宫图
t.pu()
t.goto(-100,-300)
t.pd()
t.fillcolor("red")
t.begin_fill()
t.goto(100,-100)
t.goto(100,-200)
t.goto(-100,-100)
t.goto(0,-300)
t.goto(0,-100)
t.goto(100,-300)
t.goto(-100,-200)
t.goto(-100,-300)
t.end_fill()
t.done()