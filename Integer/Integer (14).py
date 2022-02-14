# 14-misol. Uch xonali son berilgan. Uning o'ngdan birinchi raqamini o'chirib chap tarafiga yozishdan 
# hosil bo'lgan sonni aniqlaydigan dastur tuzing.
A = int(input("Uch xonali son: "))
B = A // 100
C = A // 10 % 10
D = A % 10
E = D*100+B*10+C
print("Teskari son:", E)