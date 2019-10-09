n = 0
b = []
a = int(input("请输入名字的数目:"))
print("接下来请依次输入名字\n")
while n <= a - 1:
  b.insert(0,input())
  n = n + 1
for i in b:
  print("Hello,%s!\n"%i)