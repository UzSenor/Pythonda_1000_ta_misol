# For2. a va b butun son berilgan (a<b). a va b butun sonlar orasidagi barcha butun sonlarni (a va b
# ni ham) chiqaruvchi va chiqarilgan sonlar sonini chiqaruvchi dastur tuzing.
a = int(input("A = "))
b = int(input("B = "))
if a>=b:
    print("A soni B sonidan katta yoki teng")
else:
    print("Elementlar soni:",b-a+1)
    for i in range(a, b+1):
        print(i, end=" ")
