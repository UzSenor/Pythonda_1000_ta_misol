# case17. O'quv masalalarini aniqlovchi 10-40 gacha butun son berilgan. Son kiritilganda unga mos
# sonni so'z bilan ifodalovchi dastur tuzing.
z = int(input("Masala raqami(10-40 oraliqda):"))
b=z%10
u=z//10
if b==1:
    b="bir"
elif b==2:
    b="ikki"
elif b==3:
    b="uch"
elif b==4:
    b="to'rt"
elif b==5:
    b="besh"
elif b==6:
    b="olti"
elif b==7:
    b="yetti"
elif b==8:
    b="sakkiz"
elif b==9:
    b="to'qqiz"
else:
    b=""
if u==1:
    u="O'n"
elif u==2:
    u="Yigirma"
elif u==3:
    u=="O'ttiz"
elif u==4:
    u=="Qiriq"
else:
    u="Kiritilgan son belgilangandan katta yoki kichik"
print(u, b, "ta masala")