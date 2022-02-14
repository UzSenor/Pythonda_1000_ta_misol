# case1. 1-7 bo'lgan butun sonlar berilgan. Kiritilgan songa mos hafta kunlarini chiqaradigan
# dastur tuzing.
H_K = int(input("Hafta kuni: "))
if H_K==1:
    H_K="Dushanba"
elif H_K==2:
    H_K="Seshanba"
elif H_K==3:
    H_K="Chorshanba"
elif H_K==4:
    H_K="Payshanba"
elif H_K==5:
    H_K="Juma"
elif H_K==6:
    H_K="Shanba"
elif H_K==7:
    H_K="Yakshanba"
else:
    H_K="Bunday hafta kuni yo'q"
print(H_K)