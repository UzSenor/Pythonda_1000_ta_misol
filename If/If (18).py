# 18-misol. Uchta butun son berilgan. Sonlarning ikkitasi o'zaro teng, qolgan bittasining tartib 
# raqami aniqlansin.
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if a==b!=c:
    print("Uchinchi son teng emas")
elif a==c!=b:
    print("Ikkinchi son teng emas")
elif b==c!=a:
    print("Birinchi son teng emas")
else:
    print("Uchta son ham teng yoki teng emas")