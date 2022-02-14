# case18. 100-999 gacha sonlarni so'z bilan ifodalovchi dastur tuzing.
s = int(input("Son(100-999 oraliqda):"))
b=s%10
u=s%100//10
y=s//100
if y<=0 or y>9:
    print("Kiritilgan son kichik yoki katta")
else:
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
        u="o'n"
    elif u==2:
        u="yigirma"
    elif u==3:
        u=="o'ttiz"
    elif u==4:
        u=="qiriq"
    elif u==5:
        u="ellik"
    elif u==6:
        u=="oltmish"
    elif u==7:
        u=="yetmish"
    elif u==8:
        u=="sakson"
    elif u==9:
        u=="to'qson"
    else:
        u=""
    if y==1:
        y="Bir yuz"
    elif y==2:
        y="Ikki yuz"
    elif y==3:
        y=="Uch yuz"
    elif y==4:
        y=="To'rt yuz"
    elif y==5:
        y="Besh yuz"
    elif y==6:
        y=="Olti yuz"
    elif y==7:
        y=="Yetti yuz"
    elif y==8:
        y=="Sakkiz yuz"
    elif y==9:
        y=="To'qqiz yuz"
    else:
        y=""
    print(y, u, b)