# 29-misol. A, B, C butun sonlar berilgan. Tomonlari A va B to'g'ri to'rtburchakka tomoni C bo'lgan
# kvadratdan nechta joylashtirish mumkin. To'g'ri to'rt burchakka eng ko'p joylashgan kvadrat soni va
# joylashmay qolgan qismining yuzini aniqlovchi dastur tuzing.
A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))
soni1 = A // C       # Joylashtirilgan kvadratlar soni
soni2 = B // C       # Joylashtirilgan kvadratlar soni
soni = soni1 * soni2
yuz1 = A%C * A
yuz2 = B%C * (B-B%C)
ortiqcha = yuz1+yuz2  # joylashmagan qism yuzi
print(f"Kvadrat soni {soni} va joylashmagan qism yuzi {ortiqcha}")