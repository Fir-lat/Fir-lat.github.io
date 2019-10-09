import time
def x(i):
    f = pow(i+(1-i)/2,8)
    return f
m = 50
print("倒计时开始".center(m//2,"-"))
begin = time.perf_counter()
for i in range(m+1):
    a = "="*i
    b = "-"*(m-i)
    c = (i/m)*100
    d = time.perf_counter()-begin
    print("\r{:^2.0f}秒  {:^3.0f}%[{}=>{}] {:.2f}s".format(m-i,c,a,b,d),end="")
    time.sleep(x((m-i)/80))
print("\n{:-^20}".format("倒计时结束"))