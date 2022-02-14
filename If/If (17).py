# 17-misol. A,B,C haqiqiy sonlar berilgan. Agar sonlar o'sish yoki kamayish tartibida  berilgan 
# bo'lsa, sonlar ikkilantirilsin, aks holda sonlarning ishorasi o'zgartirilsin. A,B,C ning qiymatlari 
# ekranga chiqsin
A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))
if A<B<C or C<B<A:
    print("A =", A*2, "\nB =", B*2, "\nC =", C*2)
else:
    print("A =", -A, "\nB =", -B, "\nC =", -C)