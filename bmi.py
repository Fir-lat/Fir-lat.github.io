height,weight = eval(input())
bmi = weight/(height*height)
print("BMI指数为：{:.2f}".format(bmi))
who,nat = "",""
if bmi < 18.5:
    who,nat = "slim","slim"
elif 18.5 <= bmi < 24:
    who,nat = "normal","normal"
elif 24 <= bmi <25:
    who,nat = "normal","a little fat"
elif 25 <= bmi < 28:
    who ,nat = "a little fat","a little fat"
elif 28<= bmi <30:
    who,nat = "a little fat","fat"
else:
    who,nat = "fat","fat"
print("international {},nation {}".format(who,nat))