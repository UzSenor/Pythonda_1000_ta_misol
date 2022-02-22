# For28. n butun son va x haqiqiy son berilgan(n>0, |x|>1). Quyidagi 1+x/2+1*x**2/(2*4)...(2*n-3)*x**n/(2*4*2*n) topuvchi dastur tuzing.
n = int(input("N="))
x = int(float(input("X=")))
s=1
a=1
for i in range(1, n+1):
    a*=2*i
    s+=(2*i-3)*x**i/a
print("Yig'indi:", s)
