# 22-misol. Berilgan a va b sonlarining qiymatlarini almashtiring. a va b ning yangi qiymatini ekranga chiqaring.
# 1-usul
a = int(input("A = ")) 
b = int(input("B = ")) 
a, b = b, a
print("A = ", a, "\nB = ", b)
# 2-usul
a = int(input("A = ")) 
b = int(input("B = ")) 
c = a
a = b
b = c
print("A = ", a, "\nB = ", b)
# 3-usul
a = int(input("A = ")) 
b = int(input("B = ")) 
a = a+b
b = a-b
a = a-b
print("A = ", a, "\nB = ", b)