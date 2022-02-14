# Kiritilgan uchta son 1 toq va ikkita juft
A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))
print((A%2==1 and B%2==0 and C%2==0) or 
      (A%2==0 and B%2==1 and C%2==0) or 
      (A%2==0 and B%2==0 and C%2==1))