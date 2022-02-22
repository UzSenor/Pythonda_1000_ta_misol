# For23. n butun son va x haqiqiy son berilgan(n>0). Quyidagi x-(x**3)/(3!)...-1**n*x**(2*n+1)/(2*n+1)! topuvchi dastur tuzing.
n = int(input("N="))
x = int(float(input("X=")))
s=x
a=1
ishora=-1
for i in range(3, 2*n+1,2):
    a*=i*(i-1)
    s+=ishora*x**i/a
    ishora*=-1
print("\nYig'indi:", s)
