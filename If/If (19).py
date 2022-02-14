# 19-misol. To'rtta butun son berilgan. Sonlarning uchtasi o'zaro teng, qolgan bittasining tartib 
# raqami aniqlansin.
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
d = int(input("d = "))
if a==b==c!=d:
    print("To'rtinchi son teng emas")
elif a==b==d!=c:
    print("Uchinchi son teng emas")
elif a==c==d!=b:
    print("Ikkinchi son teng emas")
elif c==b==d!=a:
    print("Birinchi son teng emas")
else:
    print("Uchta son ham teng yoki teng emas")