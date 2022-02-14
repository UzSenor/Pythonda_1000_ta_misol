# case9. Sanani bildiruvchi ikkita son berilgan D(kun) va M(oy). (Kabisa yili bo'lmagan yil sanasi 
# kiritiladi). Berilgan sanadan keyingi ifodalovchi dastur tuzing. Kabisa yilida 366 kun va kabisa yili 
# bo'lmagan yilda 365 kun bor.
oy = int(input("Oy raqami:"))
kun = int(input("Kun raqami:"))
if oy==12 and kun==31:
    print(1,".", 1)
elif (oy==1 or oy==3 or oy==5 or oy==7 or oy==8 or oy==10) and kun==31:
    print(1,".", oy+1)
elif oy==2 and kun==28:
    print(1,".", oy+1)
elif (oy==4 or oy==6 or oy==9 or oy==11) and kun==30:
    print(1,".", oy+1)
else:
    print(kun+1,".", oy)
    
# case9. Qo'shimcha
oy = int(input("Oy raqami:"))
kun = int(input("Kun raqami:"))
oylar=["yanvar", "fevral", "mart", "aprel", "may", "iyun", "iyul", "avgust", "sentabr", "oktabr",
      "noyabr", "dekabr"]
if oy==12 and kun==31:
    print(1,oylar[0])
elif oy==1 and kun==31:
    print(1,oylar[1])
elif oy==3 and kun==31:
    print(1, oylar[3])
elif oy==5 and kun==31:
    print(1, oylar[5])
elif oy==7 and kun==31:
    print(1, oylar[7])
elif oy==8 and kun==31:
    print(1, oylar[8])
elif oy==10 and kun==31:
    print(1, oylar[10])
elif oy==2 and kun==28:
    print(1,oylar[2])
elif oy==4 and kun==30:
    print(1,oylar[4])
elif oy==6 and kun==30:
    print(1, oylar[6])
elif oy==9 and kun==30:
    print(1, oylar[9])
elif oy==11 and kun==30:
    print(1, oylar[11])
else:
    print(kun+1,oylar)