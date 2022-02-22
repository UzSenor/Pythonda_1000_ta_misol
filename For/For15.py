# For15. n butun son va a haqiqiy son berilgan(n>0). a ning n inchi darajasini aniqlovchi dastur tuzing.
n = int(input("N="))
a = int(float(input("A=")))
s=1
for i in range(1, n+1):
    s*=a
print(s)
