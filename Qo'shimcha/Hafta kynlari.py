# Hafta kunlari.
Y = int(input("1-365 oraliqdagi kunni kiriting: "))
H = Y % 7
if H == 1:
    print("Dushanba")
elif H == 2:
    print("Seshanba")
elif H == 3:
    print("Chorshanba")
elif H == 4:
    print("Payshanba")
elif H == 5:
    print("Juma")
elif H == 6:
    print("Shanba")
elif H == 0:
    print("Yakshanba")