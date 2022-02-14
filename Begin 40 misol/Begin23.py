# 23-misol. A, B va C sonlar berilgan. A ning qiymatini B ga, B ning qiymatini C ga, C ning qiymatini A ga o'zlashtirilsin. A, B va C ning yangi qiymatlari ekranga chiqarilsin.
a = int(input("A = ")) 
b = int(input("B = "))
c = int(input("C = "))
a, b, c = b, c, a
print("A1 = ", a, "\nB1 = ", b, "\nC1 = ", c)