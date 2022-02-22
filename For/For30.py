# For30. n butun soni va sonlar o'qida A va B nuqta berilgan. (A,B haqiqiy son). [A,B] kesmani
# teng n ta kesmaga bo'ling. [A,B] kesmadan ajratilgan barcha nuqtalar uchun f(x)=1-sin(x)ni hisoblang
from math import sin
n = int(input("n="))
A = int(input("A="))
B = int(input("B="))
x = abs(B-A)/n
for i in np.arange(n-1):
    A+=x
    f=1-sin(A)
    print(f, end=" ")
