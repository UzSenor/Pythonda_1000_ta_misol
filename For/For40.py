# For40. A va B butun soni berilgan(A<B). A va B sonlari orasidagi barcha butun sonlarni chiqaruvchi
# dastur tuzilsin. Bunda A soni 1 marta, A+1 soni 2 marta va h.k.
A = int(input("A="))
B = int(input("B="))
for i in range(A,B+1):
    for j in range(i-A+1):
        print(i,end=" ")
    print("")
