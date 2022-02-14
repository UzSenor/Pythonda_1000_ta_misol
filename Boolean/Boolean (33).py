# 33-misol. a, b, c butun sonlar berilgan. Jumlani rostlikka tekshiring. a, b, c tomonli uchburchak yasash mumkin.
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
print(a<c and b<c and a+b > c or a<b and c<b and a+c>b or b<a and c<a and b+c>a)