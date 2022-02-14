# case3. Oy raqami berilgan. Kiritilgan oy qaysi faslga tegishli ekanini chiqaruvchi dastur tuzing.
oy = int(input("Oy:"))
if oy==1 or oy==2 or oy==12:
    oy="Qish"
elif oy==3 or oy==4 or oy==5:
    oy="Bahor"
elif oy==6 or oy==7 or oy==8:
    oy="Yoz"
elif oy==9 or oy==10 or oy==11:
    oy="Kuz"
else:
    oy="Yilda bunday oy yo'q"
print(oy)