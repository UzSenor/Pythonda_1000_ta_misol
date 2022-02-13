# 20-misol. Tekislikda berilgan ikkita nuqta (x1, y1) va (x2, y2) orasidagi masofa topilsin. M = sqrt((x2-x1)2 + (y2-y1)2)
x1 = int(input("X1 = ")) #X1 ning kordinatasi
y1 = int(input("Y1 = ")) #Y1 ning kordinatasi
x2 = int(input("X2 = ")) #X2 ning kordinatasi
y2 = int(input("Y2 = ")) #Y2 ning kordinatasi
M = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
print("Masofa: ", M)