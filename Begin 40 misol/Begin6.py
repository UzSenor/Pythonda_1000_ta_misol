# 6-misol. Paralelepipedning tomonlari a, b, c berilgan. Uning hajmi V = a * b * c va to'la sirti S = 2(ab+bc+ac) ni toping.
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
V = a*b*c
S = 2*(a*b+b*c+a*c)
print("Hajmi: ", V, "\nSirti: ", S)
