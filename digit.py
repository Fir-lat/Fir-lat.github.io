import turtle as t
import time
from random import random
def dot():
    t.fd(6)
    t.left(90)
    t.fd(25)
    t.pendown()
    t.pencolor(random(),random(),random())
    t.dot()
    t.right(180)
    t.penup()
    t.fd(50)
    t.pendown()
    t.pencolor(random(),random(),random())
    t.dot()
    t.right(180)
    t.penup()
    t.fd(25)
    t.right(90)
    t.fd(14)         
def drawline(draw):
    if draw:
        t.pencolor(random(),random(),random())
        t.fd(4)
        t.pendown()
        t.fd(42)
        t.penup()
        t.fd(4)
        t.right(90)
    else:
        t.pencolor("seashell")
        t.fd(4)
        t.pendown()
        t.fd(42)
        t.penup()
        t.fd(4)
        t.right(90)
def drawdigit(digit):
    drawline(True) if digit in [2,3,4,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,1,3,4,5,6,7,8,9] else drawline(False)
    drawline(True) if digit in [0,2,3,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,2,6,8] else drawline(False)
    t.left(90)
    drawline(True) if digit in [0,4,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,2,3,5,6,7,8,9] else drawline(False)
    drawline(True) if digit in [0,1,2,3,4,7,8,9] else drawline(False)
    t.left(180)
    t.penup()
    t.fd(10)
def drawdate(date):
    for i in date:
        if i in ["#"]:
            t.pencolor(random(),random(),random())
            t.write("年",font=("Arial", 18,"normal"))
            t.fd(50)
        elif i == "-":
            t.pencolor(random(),random(),random())
            t.write("月",font=("Arial", 18,"normal"))
            t.fd(50)
        elif i == "=":
            t.pencolor(random(),random(),random())
            t.write("日",font=("Arial", 18,"normal"))
            t.fd(50)
        elif i == "+":
            dot()
        else:
            drawdigit(eval(i))
def main():
    t.setup(1100,350,200,200)
    t.penup()
    t.fd(-500)
    t.pensize(5)
    drawdate(time.strftime("%Y#%m-%d=%H+%M+%S",time.gmtime()))
    t.hideturtle()
    t.done()
main()