m = []
n = int(input())
while n >= 1:
  m.append(input())
  n = n-1
print(m)
for i in range(len(m)//2):
  m.remove(m[-1])
print(m)