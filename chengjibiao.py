print("这是一个成绩表")
a = []
i = 0
print("请问你们班有多少人?\n")
n = int(input())
print("请依次输入同学的名字和成绩")
while i <= n-1:
  b = input()
  c = int(input())
  a.insert(-1,c)
  d = {c:b}
  i = i + 1
for x in a:
  if x >= 60:
    print(d[x]," ",x,"分","及格")
  else x < 60:
    print(d[x]," ",x,"分","不及格")