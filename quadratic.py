import math
a = float(input())
b = float(input())
c = float(input())
x = 0
y = 0
def quadratic(a,b,c):
  x = ((-b + math.sqrt(b*b - 4*a*c))/(2*a))
  y = ((-b - math.sqrt(b*b - 4*a*c))/(2*a))
  return x,y
#x,y = quadratic(a,b,c)
#print(x,y)
print(quadratic(a,b,c))