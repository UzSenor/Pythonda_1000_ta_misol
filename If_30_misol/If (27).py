# 27-misol. x haqiqiy son berilgan. Funksiyani hisoblang. f(x)=0 (x<0) <=> 
# 1 (0<=x<1 and x%2==0<=x<x%2==1) <=> -1 (x%2==1<=x<x%2==0)
x = int(float(input("x = ")))
if x<0:
    print("a = ", 0)
elif x%2==1:
    print("b = ", 1)
else:
    print("c = ", -1)