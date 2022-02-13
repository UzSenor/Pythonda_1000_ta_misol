# Kiritilgan sekundni soat, minut va sekund qilish.
s = int(input("Sekund: "))
soat = s // 3600
minut = s // 60 % 60
sek = s % 3600 % 60
print(soat, " soat ", minut, " minut ", sek, " sekunt ")