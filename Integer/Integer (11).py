# 11-misol. Uch xonali son berilgan. Uning raqamlar yig'indisini aniqlovchi dastur tuzing.
A = int(input("Uch xonali son: "))
B = A // 100
C = A // 10 % 10
D = A % 10
E = B+C+D
print("Raqamlar yig'indisi:", E)