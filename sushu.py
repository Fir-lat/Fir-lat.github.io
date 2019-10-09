s = 2
for i in range(3,101):
    q = 0
    for y in range(2,i):
        if i/y==0:
            q+=1
    if q < 1:
        s = s+i
print("{}".format(s))
    