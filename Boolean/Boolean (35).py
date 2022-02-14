# 35-misol. Shaxmat doskasining ikkita turli (x1, y1) va (x2, y2) kordinatalari berilgan (1-8 oraliqda yotuvchi butun sonlar).
# Jumlani rostlikka tekshiring. Berilgan maydon bir xil.
x1 = int(input("x1 (1-8) = "))
y1 = int(input("y1 (1-8) = "))
x2 = int(input("x2 (1-8) = "))
y2 = int(input("y2 (1-8) = "))
print(x1%2 == x2%2 == 1 and y1%2 == y2%2 == 1 or
      x1%2 == x2%2 == 0 and y1%2 == y2%2 == 1 or
      x1%2 == x2%2 == 1 and y1%2 == y2%2 == 0 or
      x1%2 == x2%2 == 0 and y1%2 == y2%2 == 0 or
      x1%2 == 1 and x2%2 == 0 and y1%2 == 0 and y2%2 == 1 or
      x1%2 == 0 and x2%2 == 1 and y1%2 == 1 and y2%2 == 0)