# 29-misol. (x, y) (x1, y1) (x2, y2) sonlar berilgan. Jumlani rostlikka tekshiring. Kordinatalari (x, y) bo'lgan nuqta
# chap yuqori cho'qqisi (x1, y1) kordinatalarga ega bo'lgan va o'ng pastkisi (x2, y2) tomonlari esa kordinata o'qiga paralell
# bo'lgan to'rtburchak ichida yotadi.
x = int(input("x = "))
y = int(input("y = "))
x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))
print((x>x1 and y<y1) and (x<x2 and y>y2))