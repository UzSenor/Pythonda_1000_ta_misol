# 24-misol. A, B va C sonlar berilgan. A ning qiymatini C ga, C ning qiymatini B ga, B ning qiymatini A ga o'zlashtirilsin. A, B va C ning yangi qiymatlari ekranga chiqarilsin.
# 1-usul
a = int(input("A = ")) 
b = int(input("B = "))
c = int(input("C = "))
a, b, c = c, a, b
print("A1 = ", a, "\nB1 = ", b, "\nC1 = ", c)
# 2-usul
a = int(input("A = ")) 
b = int(input("B = "))
c = int(input("C = "))
a = a+b+c
b = a-(b+c)
c = a-(b+c)
a = a-(b+c)
print("A1 = ", a, "\nB1 = ", b, "\nC1 = ", c)