import turtle
n = int(input("请输入圈数"))
n = n*4
color = input("请输入颜色")
turtle.pensize(2)
turtle.pencolor("%s"%str(color))
for i in range(n):
    turtle.circle(5*i,90)
turtle.goto(0,0)
turtle.done()