from sympy import *
#
# def f(t):
#     f = 2000*log(140000/(140000-2100*t))-9.8*t
#     return f
#
# x = symbols('x')
# truth = integrate(f(x),(x,8,30)).evalf()
# print(truth) #真值









n = 10 #步长,就是将(a,b)区间分为多少个块
a = 8
b = 30
h = (b-a)/n
tra_result = 0


for i in range(n):
    tra_result += 1/2*h*(f(a+i*h)+f(a+(i+1)*h))   #梯形积分算法
print(tra_result) #梯形积分值
