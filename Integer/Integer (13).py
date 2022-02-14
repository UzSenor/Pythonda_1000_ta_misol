# 13-misol. Uch xonali son berilgan. Uning birinchi raqamini o'chirib o'ng tarafiga yozishdan 
# hosil bo'lgan sonni aniqlaydigan dastur tuzing.
A = int(input("Uch xonali son: "))
B = A // 100
C = A // 10 % 10
D = A % 10
E = C*100+D*10+B
print("Teskari son:", E)