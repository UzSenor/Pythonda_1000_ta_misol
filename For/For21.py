# For21. n butun son berilgan(n>0). Quyidagi 1+(1/1!)+(1+2!)+...(1/n!) topuvchi dastur tuzing.
n = int(input("N="))
s=0
x=1
for i in range(1, n+1):
    x*=i
    s+=1/x
    print(x, end=" ")
print("\nYig'indi:", 1+s)
