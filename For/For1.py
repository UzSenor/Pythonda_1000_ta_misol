# For1. Qo'shimcha. n va k butun sonlar berilgan (n>0). k sonini n marta chiqaradigan dastur tuzing
n = int(input("N="))
k = int(input("K="))
if n<=0:
    print("Xatolik")
for i in range(n):
    print(k, end=" ")
