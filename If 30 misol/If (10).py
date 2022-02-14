# 10-misol. A va B butun sonlar berilgan. Sonlar o'zaro teng bo'lmasa A+B ni, teng bo'lsa 0 chiqsin.
# A va B ni ekranka chiqaring.
A = int(input("A = "))
B = int(input("B = "))
if A!=B:
    print(A, "+", B, "=", A+B)
else:
    print(A, "-", B, "=", 0)