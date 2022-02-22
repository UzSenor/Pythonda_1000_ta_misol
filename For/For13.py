# For13. n butun son berilgan(n>0). S=1.1-1.2+1.3... n ta o'zgaruvchi yig'indisi topilsin.
n = int(input("N = "))
s=0
s1=0
if n<=0:
    print("N soni manfiy yoki nolga teng")
else:
    for i in range(1, n+1,2):
        s+=i/10+1
    for j in range(2, n+1,2):
        s1+=j/10+1
    print(s-s1)
