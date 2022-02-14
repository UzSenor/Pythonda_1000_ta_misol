# 12-misol. Uch xonali son berilgan. Uning raqamlarini teskari qiladigan dastur tuzing.
A = int(input("Uch xonali son: "))
B = A // 100
C = A // 10 % 10
D = A % 10
E = D*100+C*10+B
print("Teskari son:", E)