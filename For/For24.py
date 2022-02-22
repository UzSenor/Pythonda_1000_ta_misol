# For24. n butun son va x haqiqiy son berilgan(n>0). Quyidagi 1-x**2/2!+x**4/4!...(-1)**n*x**(2*n)/(2*n)! topuvchi dastur tuzing.
n = int(input("N="))
x = int(float(input("X=")))
s=1
a=1
ishora=-1
for i in range(2, 2*n, 2):
    a*=i*(i-1)
    s+=ishora*x**i/a
    ishora*=-1
print("Yig'indi:", s)
