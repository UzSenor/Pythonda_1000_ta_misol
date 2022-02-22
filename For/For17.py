# For17. n butun son va a haqiqiy son berilgan(n>0). Bir sikldan foydalanib a ning 1 dan n gacha darajasini aniqlovchi va yig'indisini dastur tuzing.
n = int(input("N="))
a = int(float(input("A=")))
s=1
s1=0
for i in range(0, n+1):
    s*=a
    s1+=s
    print(s, end=" ")
print("\nYig'indi:",s1)
