# For27. n butun son va x haqiqiy son berilgan(n>0, |x|>1). Quyidagi x+1*x**3/2*3+1*3*x**5/2*4*5...(2*n-1)*x**(2*n+1)/((2*n)*(2*n+1)) topuvchi dastur tuzing.
n = int(input("N="))
x = int(float(input("X=")))
s=x
tepa = 1
past = 1
for i in range(1, n+1):
    tepa *= 2*i-1
    past *= 2*i
    s+=(tepa*x**(2*i+1))/(past*(2*i+1))
print("Yig'indi:", s)
