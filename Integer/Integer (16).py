# 16-misol. Uch xonali son berilgan. Uning o'nliklar va birliklar o'rnini almashtirishdan 
# hosil bo'lgan sonni aniqlaydigan dastur tuzing.
A = int(input("Uch xonali son: "))
B = A // 100
C = A // 10 % 10
D = A % 10
E = B*100+D*10+C
print("Teskari son:", E)