#  14-misol. Uchta son berilgan. Sonlarning avval kichigini so'ng kattasini ekranga chiqaradigan
# dastur tuzing.
a = int(input("a = "))
b = int(input("b = "))
c = int(input("C = "))
if a<b<c:
    print("Kichigi a:", a, "Kattasi c:", c)
elif a<c<b:
    print("Kichigi a:", a, "Kattasi b:", b)
elif b<a<c:
    print("Kichigi b:", b, "Kattasi c:", c)
elif b<c<a:
    print("Kichigi b:", b, "Kattasi a:", a)
elif c<b<a:
    print("Kichigi c:", c, "Kattasi a:", a)
elif c<a<b:  
    print("Kichigi c:", c, "Kattasi b:", b)
else:
    print("Sonlarda tenglik bor")