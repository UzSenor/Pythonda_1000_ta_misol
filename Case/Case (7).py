# case7. Og'irlik birliklari quyidagi tartibda berilgan(1-kilogram, 2-milligram, 3-garmm, 4-tonna,
# 5-sentiner). Og'irlik birligini bildiruvchi son berilgan(1-5 oraliqda). 
# Og'irlikni kilogramda ifodalovchi dastur tuzing.
birlik = int(input("Birlik(1-kilogram, 2-milligram, 3-garmm, 4-tonna, 5-sentiner):"))
a = int(input("A="))
if birlik==1:
    print(a, "kg = ", a, "kilogram")
elif birlik==2:
    print(a, "mg = ", a/1000000, "kilogram")
elif birlik==3:
    print(a, "g = ", a/1000, "kilogram")
elif birlik==4:
    print(a, "tonna = ", a*1000, "kilogram")
elif birlik==5:
    print(a, "ts = ", a*100, "kilogram")
else:
    print("Bunday birlik yo'q")