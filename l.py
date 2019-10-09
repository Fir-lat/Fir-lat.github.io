m = []
n = int(input())
while n>=1:
    m.append(input())
    n = n-1
print(m)
for i in m:
    if not isinstance(i,(int,float)):
        i.lower()
    else:
        print(i)
print(m)