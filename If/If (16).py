# 16-misol. A,B,C haqiqiy sonlar berilgan. Agar sonlar o'sish tartibida berilgan bo'lsa, sonlar
# ikkilantirilsin, aks holda sonlarning ishorasi o'zgartirilsin. A,B,C ning qiymatlari ekranga chiqsin
A = float(input("A = "))
B = float(input("B = "))
C = float(input("C = "))
if A<B<C:
    print("A=", A*2, "\nB=", B*2, "\nC=", C*2)
else:
    print("A=", -A, "\nB=", -B, "\nC=", -C)