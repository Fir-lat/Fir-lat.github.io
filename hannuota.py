def move(n, a, b, c):
    if(n == 1):
        print(a,"->",c)
        return
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)
n = int(input())
move(n, "a", "b", "c") 