# 11-misol. A va B butun sonlar berilgan. Sonlar o'zaro teng bo'lmasa sonlarning kattasini, 
# teng bo'lsa 0 o'zlashtirsin. A va B ni ekranka chiqaring.
A = int(input("A = "))
B = int(input("B = "))
if A>B:
    print("Kattasi A=", A)
elif A<B:
    print("Kattasi B=", B)
else:
    print(A, "va", B, 0)