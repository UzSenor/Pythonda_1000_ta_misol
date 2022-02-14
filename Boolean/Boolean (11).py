# 11-misol. Ikkita A va B butun sonlari berilgan. Jumlani rostlikka tekshiring. A va B sonalri 
# ikkalasi ham toq yoki ikkalasi ham juft son.
A = int(input("A = "))
B = int(input("B = "))
print((A%2 == 1 and B%2 == 1) or (A%2 == 0 and B%2 == 0))