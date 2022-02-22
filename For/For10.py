# For10. n butun son berilgan(n>0). S=1+1/2+1/3...1/n yig'indisi topilsin.
n = int(input("N = "))
s=0
if n<=0:
    print("N soni manfiy yoki nolga teng")
else:
    for i in range(1, n+1):
        s+=1/i
    print(s)
