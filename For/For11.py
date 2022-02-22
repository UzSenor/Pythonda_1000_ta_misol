# For11. n butun son berilgan(n>0). S=n**2+(n+1)**2...(2*n)**2 yig'indisi topilsin.
n = int(input("N = "))
s=0
if n<=0:
    print("N soni manfiy yoki nolga teng")
else:
    for i in range(0, n+1):
        s+=(n+i)**2
    print(s)
