# Berilgan sanaga 2 kun qo'shish
kun = int(input("Kun raqami:"))
oy = int(input("Oy raqami:"))
yil = int(input("Yil raqami: "))

kabisa=False
if yil%4==0:
    kabisa=True
if yil>100 and yil%400!=0:
    kabisa=False

kun=kun+2

if oy==1 or oy==3 or oy==5 or oy==7 or oy==8 or oy==10:
    if kun==33:
        kun=2
        oy=oy+1
    if kun==32:
        kun=1
        oy=oy+1
if oy==4 or oy==6 or oy==9 or oy==11:
    if kun==32:
        kun=2
        oy=oy+1
    if kun==31:
        kun=1
        oy=oy+1
if oy==12:
    if kun==33:
        kun=2
        oy==1
        yil=yil+1
    if kun==32:
        kun=1
        oy==1
        yil=yil+1
if oy==2:
    if kun==30+kabisa:
        kun=2
        oy=oy+1
    if kun==29+kabisa:
        kun=1
        oy=oy+1
        
print(kun,oy,yil, sep=".")