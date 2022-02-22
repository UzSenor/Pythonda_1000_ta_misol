# For12. n butun son berilgan(n>0). S=1.1*1.2*1.3... n ta ko'paytuvchi topilsin.
n = int(input("N = "))
s=1
if n<=0:
    print("N soni manfiy yoki nolga teng")
else:
    for i in range(1, n+1):
        s*=i/10+1
    print(s)
