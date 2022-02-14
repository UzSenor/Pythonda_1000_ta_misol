# case15. O'yin kartasi turlari berilgan. 1-g'isht, 2-olma, 3-chillak, 4-qarg'a. 10 lik kartadan
# katta kartalar quyidagi qiymatni o'zlashtirsin. 11-valet, 12-dama, 13-qirol, 14-tuz. Ikkita butun 
# son berilgan N-karta raqami(6<=N<=14), M-karta turi(1<=M<=4) kiritilganda Karta nomlarini(masalan:
# olti qarg'a) chiqaruvchi dastur tuzilsin.
N = int(input("Karta raqami(6<=N<=14):"))
M = int(input("Karta turi(1<=M<=4):"))
if N==6:
    N="Olti"
elif N==7:
    N="Yetti"
elif N==8:
    N="Sakkiz"
elif N==9:
    N="To'qqiz"
elif N==10:
    N="O'n"
elif N==11:
    N="Valet"
elif N==12:
    N="Dama"
elif N==13:
    N="Qirol"
elif N==14:
    N="Tuz"
else:
    N="Bunday raqamli karta yo'q"
if M==1:
    M="g'isht"
elif M==2:
    M="olma"
elif M==3:
    M="chillak"
elif M==4:
    M="qarg'a"
else:
    M="Bunday karta turi yo'q"
print(N, M)