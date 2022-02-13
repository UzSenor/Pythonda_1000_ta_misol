# 17-misol. Sonlar o'qida a, b, c nuqtalar berilgan. ac va bc kesmalar uzunligi va kesmalar uzunligining yig'indisini toping.
a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))
ac = abs(c-a)
bc = abs(c-b)
yigindi = ac+bc
print("AC kesma: ", ac, "\nBC kesma: ", bc, "\nYig'indi: ", yigindi)