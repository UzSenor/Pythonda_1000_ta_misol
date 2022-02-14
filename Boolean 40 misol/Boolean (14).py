# 14-misol. Uchta A, B va C butun sonlar berilgan. Jumlani rostlikka tekshiring. A, B, C sonlarning
# faqat bittasi musbat.
A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))
x = A>0 and B<0 and C<0
y = B>0 and A<0 and C<0
z = C>0 and A<0 and B<0
print(x or y or z)