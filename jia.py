s = 0
a = [1,2,3,4,5,6]
print(a)
print(len(a))
for b in a:
  s = s + b
print(s)
c = int(input("Please input a number\n"))
d = 0
while c>0:
  d = d + c
  c = c - 1
print("c = %d,The sum is %d"%(c,d))
