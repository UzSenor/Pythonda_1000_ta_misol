# 23-misol. Kordinata o'qiga paralell joylashgan to'g'ri to'rtburchakning uchta uchining kordinatasi
# berilgan. To'rtinchi uchini aniqlaydigan dastur tuzing.
# (x1,y1)________________(x4,y4)
#       |               |
#       |               |
# (x2,y2)_______________(x3, y3)

x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))
x3 = int(input("x3 = "))
y3 = int(input("y3 = "))
if x1==x2 and y2==y3:
    x4=x3
    y4=y1
    print("x4=", x4, "y4=", y4)
else:
    print("Berilgan nuqtalar to'g'ri to'rtburchak emas.")