#dayday
def dayUP(df):
    dayup = 1
    for i in range(365):
        if i%7 in [6,0]:
            dayup = dayup * (1 - 0.01)
        else:
            dayup = dayup*(1+df)
    return dayup
dayu = float(input())
while dayUP(dayu) < 37.78:
    dayu += 0.001
print("{:.6f}".format(dayu))