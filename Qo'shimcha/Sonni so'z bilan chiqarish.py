# Qo'shimcha. N son berilgan(1<=N<=99). Shu sonni yozuv ko'rinishda ekranga chiqaring.
N = int(input("N = "))
bir = N%10
un = N//10
if un==1:
    un="o'n"
elif un==2:
    un="yigirma"
elif un==3:
    un="o'ttiz"
elif un==4:
    un="qiriq"
elif un==5:
    un="ellik"
elif un==6:
    un="oltmish"
elif un==7:
    un="yetmish"
elif un==8:
    un="sakson"
elif un==9:
    un="to'qson"
else:
    un=""
if bir==1:
    bir="bir"
elif bir==2:
    bir="ikki"
elif bir==3:
    bir="uch"
elif bir==4:
    bir="to'rt"
elif bir==5:
    bir="besh"
elif bir==6:
    bir="olti"
elif bir==7:
    bir="yetti"
elif bir==8:
    bir="sakkiz"
elif bir==9:
    bir="to'qqiz"
else:
    bir=""
print(un, bir)