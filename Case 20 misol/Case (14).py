# case14. Tengtomonli uchburchakning tomonlari elementlari quyidagicha tartiblangan. 1-tomon a, 
# 2-ichki aylana radiusi R1=a*3**0.5/6, 3-Tashqi aylana radiusi R2=2*R1, 4-yuzi S=a**2*3**0.5/4.
# Shu elementlarning bittasi berilganda qolgani topilsin.
e = int(input("Element raqmi(1-tomon, 2-ichki aylana R1, 3-tashqi aylana R2, 4-yuza):"))
if e==1:
    a=int(input("Tomonni kiriting:"))
    print("Tomon:", a)
    print("Ichki radus:", a*3**0.5/6)
    print("Tashqi radius:", a*3**0.5/3)
    print("Yuza:", a**2*3**0.5/4)
if e==2:
    R1=int(input("Ichki radiusni kiriting:"))
    print("Tomon:", (6*R1)/3**0.5)
    print("Ichki radius:", R1)
    print("Tashqi radius:", 2*R1)
    print("Yuza:", 3*3**0.5*R1**2)
if e==3:
    R2=int(input("Tashqi radiusni kiriting:"))
    print("Tomon:", (3*R2)/3**0.5)
    print("Ichki radius:", R2/2)
    print("Tashqi radius:", R2)
    print("Yuza:", (3*3**0.5*R2**2)/2)
if e==4:
    S=int(input("Yuzani kiriting:"))
    print("Tomon:", 2*(S/3**0.5)**0.5)
    print("Ichki radius:", (S/(3*3**0.5))**0.5)
    print("Tashqi radius:", ((2*S)/(3*3**0.5))**0.5)
    print("Yuza:", S)