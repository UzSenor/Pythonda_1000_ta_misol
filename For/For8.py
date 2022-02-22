# For8. a va b butun son berilgan (a<b). a va b butun sonlar orasidagi sonlar ko'paytmasi topilsin.
a = int(input("A = "))
b = int(input("B = "))
s=1
if a>=b:
    print("A soni B sonidan katta yoki teng")
for i in range(a, b+1):
    s*=i
print(s)
