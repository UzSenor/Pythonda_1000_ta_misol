# case8. Sanani bildiruvchi ikkita son berilgan D(kun) va M(oy). (Kabisa yili bo'lmagan yil sanasi 
# kiritiladi). Berilgan sanani ifodalovchi dastur tuzing. Kabisa yilida 366 kun va kabisa yili 
# bo'lmagan yilda 365 kun bor.
oy = int(input("Oy raqami:"))
kun = int(input("Kun raqami: "))
if oy==1 and kun<=31:
    print(kun, "yanvar")
elif oy==2 and kun<=28:
    print(kun, "fevral")
elif oy==3 and kun<=31:
    print(kun, "mart")
elif oy==4 and kun<=30:
    print(kun, "aprel")
elif oy==5 and kun<=31:
    print(kun, "may")
elif oy==6 and kun<=30:
    print(kun, "iyun")
elif oy==7 and kun<=31:
    print(kun, "iyul")
elif oy==8 and kun<=31:
    print(kun, "avgust")
elif oy==9 and kun<=30:
    print(kun, "sentabr")
elif oy==10 and kun<=31:
    print(kun, "oktabr")
elif oy==11 and kun<=30:
    print(kun, "noyabr")
elif oy==12 and kun<=31:
    print(kun, "dekabr")
elif oy>12 and kun<=31:
    print("Bunday oy yo'q")
else:
    print("Bunday kun yo'q")
    
# case8. Qo'shimcha
oy = int(input("Oy raqami:"))
kun = int(input("Kun raqami:"))
if (oy==1 or oy==3 or oy==5 or oy==7 or oy==8 or oy==10 or oy==12) and kun<=31:
    print(kun,".",oy)
elif oy==2 and kun<=28:
    print(kun,".",oy)
elif (oy==4 or oy==6 or oy==9 or oy==11) and kun<=30:
    print(kun,".",oy)
else:
    print("Bunday oy yoki kun yo'q")