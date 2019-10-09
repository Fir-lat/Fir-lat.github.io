def getnum():
    i = input()
    while i != "":
        num.append(eval(i))
        i = input()
    return num
num = []
getnum()
print(num)