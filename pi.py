from random import random
from time import perf_counter
n = 1000*10000
x = 0
pi = 0
t = perf_counter()
for i in range(n):
    a,b=random(),random()
    l = pow(pow(a,2)+pow(b,2),0.5)
    if l <= 1:
        x += 1
pi = 4*x/n
print("Π={:.16f}".format(pi))
print("{:.6f}".format(perf_counter()-t))