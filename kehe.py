import turtle as t
from random import random
def kh(lenth,n):
    if n == 0:
        t.fd(lenth)
    else:
        for i in [0,90,-90,-90,90]:
            t.left(i)
            kh(lenth/3,n-1)
def ad():
    for i in range(4):
        t.pencolor(random(),random(),random())
        kh(10,3)
        t.right(90)
def main():
    t.setup(1000,600)
    t.pu()
    t.goto(0,0)
    t.pd()
    t.pensize(2)
    t.left(30)
    ad()
    t.hideturtle()
    t.done()
main()