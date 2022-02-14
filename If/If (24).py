# 24-misol. x haqiqiy son berilgan. funksiyani hisoblang. f(x)=2*sin(x) <=> x-6  x>0 <=> x<=0
from math import *
x = float(input("x = "))
if x>0:
    print("a = ",2*sin(x))
else:
    print("b = ",x-6)