a=input().split()
m = eval(a[0])
x = a[1]
n = eval(a[2])
if x in ["+"]:
    m = m+n
    print("{:.2f}".format(m))
elif x in ["-"]:
    m = m-n
    print("{:.2f}".format(m))
elif x in ["*"]:
    m = m*n
    print("{:.2f}".format(m))
else:
    m = m/n
    print("{:.2f}".format(m))