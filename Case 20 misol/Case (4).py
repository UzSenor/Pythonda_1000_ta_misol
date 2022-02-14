# case4. Oy raqami berilgan. kiritilgan oyda nechta kun borligini aniqlovchi dastur tuzing.
oy = int(input("Oy raqami:"))
if oy==1 or oy==3 or oy==5 or oy==7 or oy==8 or oy==10 or oy==12:
    oy=31
elif oy==2:
    oy=28
else:
    oy=30
print(oy, "kun bor")