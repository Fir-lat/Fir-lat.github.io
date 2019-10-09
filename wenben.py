a = open("hamlet.txt",'r',encoding="utf-8")
txt = a.readline()
#a.close()
s = 0
n = 0
for line in a:
    if len(line) != 0:
        for i in line:
            s += 1
        n += 1
print(s,n)
m = s/n
q = round(m)
print(q)