# For39. A va B butun soni berilgan(A<B). A va B sonlari orasidagi barcha butun sonlarni chiqaruvchi
# dastur tuzilsin. Bunda har bir son o'zining qiymaticha chiqarilsin. Yani 3 soni 3 marta chiqarilsin
A = int(input("A="))
B = int(input("B="))
for i in range(A,B+1):
    for j in range(i):
        print(i,end=" ")
    print("")
