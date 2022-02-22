# For25. n butun son va x haqiqiy son berilgan(n>0, |x|>1). Quyidagi x-x**/2+x**3/3...(-1)**n-1*x**n/n topuvchi dastur tuzing.
n = int(input("N="))
x = int(float(input("X=")))
s=0
for i in range(1, n+1):
    s+=(-1)**(i-1)*x**i/i
print("Yig'indi:", s)
