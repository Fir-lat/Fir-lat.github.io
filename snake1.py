import turtle as t
m = 1
t.setup(1000,600)
t.pu()
t.goto(-200,0)
t.pd()
t.pensize(m)
t.pencolor("grey")
t.seth(-30)
for i in range(4):
    m = m+1
    t.pensize(m)
    t.circle(80,60)
    m = m+1
    t.pensize(m)
    t.circle(-40,60)
t.circle(80,30)
t.fd(40)
t.circle(10,180)
t.circle(-10,180)
t.fd(30)
t.done()