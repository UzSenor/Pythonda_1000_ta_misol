# 18-misol. 999 sondan katta son berilgan. Bir marta bo'lib butunni va bo'lib qoldiqni olish 
# operatsiyasidan foydalanib berilgan sonning mingliklar xonasidagi raqamni aniqlaydigan dastur
# tuzing.
A = int(input("999 dan katta son: "))
B = A % 10000 // 1000
print("Mingliklar xonasidagi son:", B)