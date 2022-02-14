# Berilgan sanadan oldingi sanani topish
kun = int(input("Kun raqami:"))
oy = int(input("Oy raqami:"))
yil = int(input("Yil raqami: "))

kabisa=False
if yil%4==0:
    kabisa=True
if yil>100 and yil%400!=0:
    kabisa=False
    
kun = kun-1
if oy==5 or oy==7 or oy==10 or oy==12:
    if kun==0:
        kun=30
        oy=oy-1
elif oy==2 or oy==4 or oy==6 or oy==9 or oy==11 or oy==8:
    if kun==0:
        kun=31
        oy=oy-1
elif oy==3:
    if kun==0:
        kun=28+kabisa
elif oy==1:
    if kun==0:
        kun=31
        oy=12
        yil=yil-1
print(kun,oy,yil, sep=".")