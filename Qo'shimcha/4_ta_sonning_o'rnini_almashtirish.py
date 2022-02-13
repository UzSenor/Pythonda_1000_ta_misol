# Kiritilgan 4 ta sonning o'rnini almashtirish
a = int(input("A = ")) 
b = int(input("B = "))
c = int(input("C = "))
d = int(input("D = "))
a = a+b+c+d
b = a-(b+c+d)
c = a-(b+c+d)
d = a- (b+c+d)
a = a-(b+c+d)
print("A1 = ", a, "\nB1 = ", b, "\nC1 = ", c, "\nD1 = ", d)