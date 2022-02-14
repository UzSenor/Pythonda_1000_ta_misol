# 15-misol. Uch xonali son berilgan. Uning o'nliklar va yuzliklar raqamlarining o'rnini almashtirishdan 
# hosil bo'lgan sonni aniqlaydigan dastur tuzing.
A = int(input("Uch xonali son: "))
B = A // 100
C = A // 10 % 10
D = A % 10
E = C*100+B*10+D
print("Teskari son:", E)