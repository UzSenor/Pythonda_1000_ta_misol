# 17-misol. 999 sondan katta son berilgan. Bir marta bo'lib butunni va bo'lib qoldiqni olish 
# operatsiyasidan foydalanib berilgan sonning yuzliklar xonasidagi raqamni aniqlaydigan dastur
# tuzing.
A = int(input("999 dan katta son: "))
B = A % 1000 // 100
print("Yuzliklar xonasidagi son:", B)