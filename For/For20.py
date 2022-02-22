# For20. n butun son berilgan(n>0). bitta for dan foydalanib 1!+2!+...n! topuvchi dastur tuzing.
n = int(input("N="))
s=0
x=1
if n<=0:
    print("Kiritilgan son nolga teng yoki manfiy")
else:
    for i in range(1, n+1):
        x*=i
        s+=x
        print(x, end=" ")
    print("\nYig'indi:", s)
