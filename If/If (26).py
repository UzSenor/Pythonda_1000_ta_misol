# 26-misol. x haqiqiy son berilgan. Funksiyani hisoblang. f(x)=-x (x<=0) <=> x**2 (0<x<2) <=> 4 (2<=x)
x = float(input("x = "))
if x<=0:
    print("a = ", -x)
elif 0<x<2:
    print("b = ", x**2)
else:
    print("c = ", 4)