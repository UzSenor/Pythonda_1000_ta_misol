# 34-misol. Shaxmat doskasining (x, y) kordinatalari berilgan. (1-8 oraliqda yotuvchi butun sonlar) doskaning chap pastki 
# burchagi (1, 1) qoraligini hisobga olib jumlani rostlikka tekshiring. Berilgan x, y katak oq.
x = int(input("x (1-8) = "))
y = int(input("y (1-8) = "))
print(x%2 == 1 and y%2 == 0 or x%2 == 0 and y%2 == 1)