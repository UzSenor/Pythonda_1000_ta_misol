#  15-misol. Uchta son berilgan. Sonlarning yig'indisi eng kattasini ekranga chiqaradigan
# dastur tuzing.
a = int(input("a = "))
b = int(input("b = "))
c = int(input("C = "))
if a<b<=c or a<c<=b:
    print("Katta yig'indi:", b+c)
elif b<a<=c or b<c<=a:
    print("Katta yig'indi:", a+c)
else:
    print("Katta yig'indi:", a+b)