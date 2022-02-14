# 21-misol. Uchburchakning uchta tomoni uchlari koordinatalari berilgan (x1, y1), (x2, y2), (x3, y3). Ikkita nuqta ikkita nuqta orasidagi masofani topish 20-misolda berilgan. Uchburchakning yuzi va peremetrini toping.
x1 = int(input("X1 = ")) #X1 ning kordinatasi
y1 = int(input("Y1 = ")) #Y1 ning kordinatasi
x2 = int(input("X2 = ")) #X2 ning kordinatasi
y2 = int(input("Y2 = ")) #Y2 ning kordinatasi
x3 = int(input("X3 = ")) #X3 ning kordinatasi
y3 = int(input("Y3 = ")) #Y3 ning kordinatasi
a = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
b = ((x3-x1)**2 + (y3-y1)**2)**(1/2)
c = ((x3-x2)**2 + (y3-y2)**2)**(1/2)
p = (a+b+c)/2
S = (p*(p-a)*(p-b)*(p-c))**(1/2)
print("Peremetiri: ", p, "\nYuzasi: ", S)