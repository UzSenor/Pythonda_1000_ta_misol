# 39-misol. A, B, C koifisentlar berilgan. A * x ** 2 + B * x + C = 0 kvadrat tenglamaning diskriminanti noldan katta bo'lsa uning yechimini aniqlaydigan dastur tuzing. x1 = (-B-(D) * (1/2)), x2 = (-B+(D) * (1/2)), D = B ** 2 - 4 * A * C
A = int(input("A koifisent: "))
B = int(input("B koifisent: "))
C = int(input("C koifisent: "))
D = B**2-4*A*C
x1 = (-B-(D) * (1/2))
x2 = (-B+(D) * (1/2))
print("X1 = ", x1, "\nX2 = ", x2)