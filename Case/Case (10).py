# case10. Robot faqat to'rtta tomonga ko'cha oladi(s-shimol, j-janub, q-sharq, g-g'arb) va uchta 
# raqamli komanda: 0-o'ngga, 1-chapga buril, 2-180 gradusga burul. C-lakatorning boshlang'ich holati
# va K1, K2 komandalar berilgan. Berilgan komanda bajarilgandan keyin lokatr holatini aniqlang.
c = input("Loaktor holati(s-shimol, j-janub, q-sharq, g-g'arb):")
K1 = int(input("1-komanda(0-o'ngga, 1-chapga buril, 2-180 gradusga burul):"))
K2 = int(input("2-komanda(0-o'ngga, 1-chapga buril, 2-180 gradusga burul):"))
if c=="s":
    if K1==K2==0 or K1==K2==1:
        print("janub")
    elif K1==0 and K2==1 or K1==1 and K2==0 or K1==K2==2:
        print("shimol")
    elif K1==0 and K2==2 or K1==2 and K2==0:
        print("sharq")
    else:
        print("g'arb")
if c=="j":
    if K1==K2==0 or K1==K2==1:
        print("shimol")
    elif K1==0 and K2==1 or K1==1 and K2==0 or K1==K2==2:
        print("janub")
    elif K1==0 and K2==2 or K1==2 and K2==0:
        print("g'arb")
    else:
        print("sharq")
if c=="q":
    if K1==K2==0 or K1==K2==1:
        print("g'arb")
    elif K1==0 and K2==1 or K1==1 and K2==0 or K1==K2==2:
        print("sharq")
    elif K1==0 and K2==2 or K1==2 and K2==0:
        print("shimol")
    else:
        print("janub")
if c=="g":
    if K1==K2==0 or K1==K2==1:
        print("sharq")
    elif K1==0 and K2==1 or K1==1 and K2==0 or K1==K2==2:
        print("g'arb")
    elif K1==0 and K2==2 or K1==2 and K2==0:
        print("janub")
    else:
        print("shimol")
        