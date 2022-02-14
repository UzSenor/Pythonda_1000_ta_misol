# 9-misol. A va B haqiqiy sonlar berilgan. Shu sonlarni shunday o'zgartirish kerakki A son kichik
# B son katta bo'lsin. A va B ni ekranka chiqaring.
A = float(input("A = "))
B = float(input("B = "))
C = A - B
if A>B:
    print(A, "va", B+C+1)
elif A<B:
    print(A, "va", B)
else:
    print(A, "va", B+1)