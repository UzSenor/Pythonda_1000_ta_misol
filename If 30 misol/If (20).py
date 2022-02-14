# 20-misol. Sonalar o'qida A,B,C nuqtalar berilgan. A nuqtaga eng yaqin nuqta va ular orasidagi 
# masofa topilsin.
A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))
x = abs(A-B)
y = abs(A-C)
if x<y:
    print("Yaqin nuqta B, orasidagi masifa", x)
else:
    print("Yaqin nuqta C, orasidagi masofa", y)