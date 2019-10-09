n = int(input())
def l(n):
    i,a,b=0,0,1
    while i < n:
        yield b
        a,b=b,a+b
        i = i+1
    return 'done'
l(n)
while True:
    try:
        x = next(l)
        print("l:",x)
    except Stoplteration as e:
        print('Generator return value::',e.value)
        break