#  13-misol. Uchta son berilgan. Sonlarning o'rtachasi(ya'ni katta-kichik o'rtasidagi son)ni
# aniqlaydigan dastur tuzing.
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if b<a<c or c<a<b:
    print("O'rtachasi a:",a)
elif a<b<c or c<b<a:
    print("O'rtachasi b:",b)
else:  
    print("O'rtachasi c:",c)