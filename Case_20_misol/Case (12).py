# case12. Doiraning elementlari quyidagicha tartiblangan. 1-radius R, 2-diametr D=2*R, 3-uzunligi 
# L=2*pi*R, 4-yuzi S=pi*R**2. Shu elementlarning bittasi berilganda qolgani topilsin.
e = int(input("Element raqmi(1-radius, 2-diametr, 3-uzunlik, 4-yuza):"))
pi=3.14
if e==1:
    R=int(input("Radiusni kiriting:"))
    print("Radius:", R)
    print("Diametr:", 2*R)
    print("Uzunlik:", 2*pi*R)
    print("Yuza:", pi*R**2)
if e==2:
    D=int(input("Diametrni kiriting:"))
    print("Radius:", D/2)
    print("Diametr:", D)
    print("Uzunlik:", pi*D)
    print("Yuza:", pi*(D/2)**2)
if e==3:
    L=int(input("Uzunlikni kiriting:"))
    print("Radius:", L/(2*pi))
    print("Diametr:", L/pi)
    print("Uzunlik:", L)
    print("Yuza:", L**2/4*pi)
if e==4:
    S=int(input("Yuzani kiriting:"))
    print("Radius:", (S/pi)**0.5)
    print("Diametr:", 2*(S/pi)**0.5)
    print("Uzunlik:", 2*(S*pi)**(1/2))
    print("Yuza:", S)