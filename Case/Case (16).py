# case16. Yoshni yillarda hisoblovchi 20-69 gacha butun son berilgan. Son kiritilganda so'z bilan
# ekranga chiqaruvchi dastur tuzing.(yigirma yosh, qiriq uch yosh)
y = int(input("Yoshingiz(20-69 oraliqda):"))
b=y%10
u=y//10
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
if u==2:
    u="Yigirma"
elif u==3:
    u=="O'ttiz"
elif u==4:
    u=="Qiriq"
elif u==5:
    u=="Ellik"
elif u==6:
    u=="Oltmish"
else:
    u="Kiritilgan yosh belgilangandan katta yoki kichik"
print(u, b, "yosh")