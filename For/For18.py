# For18. n butun son va a haqiqiy son berilgan(n>0). S=1-a+a**2-a**3...(-1)**n*a**n bir sikldan foydalanib darajani va yig'indisi topilsin.
n = int(input("N = "))
a = int(float(input("A = ")))
s=0
if n<=0:
    print("N soni manfiy yoki nolga teng")
else:
    for i in range(1, n+1):
        s+=(-a)**i
    print("\nYig'indi:",1+s)
