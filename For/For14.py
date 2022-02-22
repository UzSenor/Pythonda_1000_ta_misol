# For14. n butun son berilgan(n>0). Sonning kvadratini quyidagi formula orqali toping. n**2=1+3+...(2*n-1)
n = int(input("N = "))
s=0
if n<=0:
    print("N soni manfiy yoki nolga teng")
else:
    for i in range(1, n+1,2):
        s+=i
    print(s)
