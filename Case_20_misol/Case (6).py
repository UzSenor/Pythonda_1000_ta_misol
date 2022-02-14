# case6. Uzunlik birliklari quyidagi tartibda berilgan(1-desimetr, 2-kilometr, 3-metr, 4-millimetr,
# 5-santimetr). Uzunlik birligini bildiruvchi son berilgan(1-5 oraliqda) va shu uzunlikda kesma 
# berilgan. Kesma uzunligini metrda ifodalovchi dastur tuzing.
birlik = int(input("Birlik(1-desimetr, 2-kilometr, 3-metr, 4-millimetr, 5-santimetr):"))
a = int(input("A="))
if birlik==1:
    print(a, "dm = ", a/10, "metr")
elif birlik==2:
    print(a, "km = ", a*1000, "metr")
elif birlik==3:
    print(a, "m = ", a, "metr")
elif birlik==4:
    print(a, "mm = ", a/1000, "metr")
elif birlik==5:
    print(a, "sm = ", a/100, "metr")
else:
    print("Bunday birlik yo'q")