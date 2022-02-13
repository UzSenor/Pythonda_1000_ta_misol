# Kiritilgan 3 xonali sonni teskari qilish.
a = int(input("Uch xonali son: "))
yuz = a // 100
un = a % 100 // 10
bir = a % 10
print(bir*100+un*10+yuz*1)