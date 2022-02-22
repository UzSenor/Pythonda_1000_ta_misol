# For29. n butun soni va sonlar o'qida A va B nuqta berilgan. (A,B haqiqiy son). [A,B] kesmani
# teng n ta kesmaga bo'ling. [A,B] kesmadan ajratilgan barcha nuqtalarni chiqaring
n = int(input("n="))
A = int(input("A="))
B = int(input("B="))
x = abs(B-A)/n
for i in range(n-1):
    A+=x
    print(A, end=" ")
