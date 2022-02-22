# For22. n butun son va x haqiqiy son berilgan(n>0). Quyidagi 1+x+(x**2)/(2!)...x**n/n! topuvchi dastur tuzing.
n = int(input("N="))
x = int(float(input("X=")))
s=0
a=1
if n<=0:
    print("Kiritilgan son nolga teng yoki manfiy")
else:
    for i in range(1, n+1):
        a*=i
        s+=x**i/a
        print(a, end=" ")
    print("\nYig'indi:", 1+s)
