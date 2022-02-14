# 40-misol. A1, B1, C1, A2, B2, C2 koiffisentlari berilgan chiziqli tenglamalar sistemasining yechimini aniqlaydigan dastur tuzing.
A1 = int(input("A1 koifisent: "))
B1 = int(input("B1 koifisent: "))
C1 = int(input("C1 koifisent: "))
A2 = int(input("A2 koifisent: "))
B2 = int(input("B2 koifisent: "))
C2 = int(input("C2 koifisent: "))
D = A1*B2 - A2*B1
x = (C1*B2-C2*B1)/D
y = (A1*C2 - A2*C1)/D
print("x = ", x, "\ny = ", y)