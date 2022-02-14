# case13. Tengyonli uchburchakning tomonlari elementlari quyidagicha tartiblangan. 1-Katet a, 
# 2-gipatenuza c=a*2**0.5, 3-gipatenuzaga tushurilgan balandlik h=c/2, 4-yuzi S=(c*h)/2.
# Shu elementlarning bittasi berilganda qolgani topilsin.
e = int(input("Element raqmi(1-katet, 2-gipatenuza, 3-balandlik, 4-yuza):"))
if e==1:
    a=int(input("Katetni kiriting:"))
    print("Katet:", a)
    print("Gipatenuza:", a*2**0.5)
    print("Balandlik:", (a*2**0.5)/2)
    print("Yuza:", a**2/2)
if e==2:
    c=int(input("Gipatenuzani kiriting:"))
    print("Katet:", c/2**0.5)
    print("Gipatenuza:", c)
    print("Balandlik:", c/2)
    print("Yuza:", c**2/4)
if e==3:
    h=int(input("Balandlik kiriting:"))
    print("Katet:", h*8**0.5)
    print("Gipatenuza:", 2*h)
    print("Balandlik:", h)
    print("Yuza:", h**2)
if e==4:
    S=int(input("Yuzani kiriting:"))
    print("Katet:", (S*2)**0.5)
    print("Gipatenuza:", (S*4)**0.5)
    print("Balandlik:", S**0.5)
    print("Yuza:", S)