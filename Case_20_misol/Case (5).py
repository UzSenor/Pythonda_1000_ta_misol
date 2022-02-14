# case5. a va b butun son va amal butun soni berilgan. a va b sonlar ustida amal bajaruvchi dastur 
# tuzing. 1-qo'shish, 2-ayirish, 3-bo'lish, 4-ko'paytirish
a = int(input("A="))
b = int(input("B="))
amal = int(input("Amal raqami(1-qo'shish, 2-ayirish, 3-bo'lish, 4-ko'paytirish):"))
if amal==1:
    print(a,"+",b,"=",a+b)
elif amal==2:
    print(a,"-",b,"=",a-b)
elif amal==3:
    print(a,":",b,"=",a/b)
elif amal==4:
    print(a,"*",b,"=",a*b)
else:
    print("Bunday amal yo'q")