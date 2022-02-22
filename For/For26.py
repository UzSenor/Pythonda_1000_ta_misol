# For26. n butun son va x haqiqiy son berilgan(n>0, |x|>1). Quyidagi x-x**3/3+x**5/5...(-1)**n*x**(2*n+1)/(2*n+1) topuvchi dastur tuzing.
n = int(input("N="))
x = int(float(input("X=")))
s=x
ishora=-1
for i in range(3, 2*n+1,2):
    s+=ishora*x**i/i
    ishora*=-1
print("Yig'indi:", s)
