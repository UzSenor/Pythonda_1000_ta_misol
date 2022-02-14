# case20. Ikkita burj vaqtlarini aniqlovchi son berilgan D(kun) va M(oy). Berilgan sana qaysi
# burj ekanini aniqlovchi dastur tuzing. "Qovg'a 20.01-18.02", "Baliq 19.02-20.03", "Qo'y 21.03-19.04"
# "Buzoq 20.04-20.05", "Egizaklar 21.05-21.06", "Qisqichbaqa 22.06-22.07", "Arslon 23.07-22.08",
# "Parizod 23.08-22.09", "Tarozi 23.09-22.10", "Chayon 23.10-22.11", "O'qotar 23.11-21.12", "Echki
# 22.12-19.01"
D = int(input("Kun:"))
M = int(input("Oy: "))
if M==1 or M==3 or M==5 or M==7 or M==8 or M==10 or M==12:
    D=31
elif M==2:
    D=28
elif M==4 or M==6 or M==9 or M==11:
    D=30
else:
    print("Bunday oy yoki kun yo'q")
if D>=20 and M==1 or D<=18 and M==2:
    print("Qovg'a")
elif D>=19 and M==2 or D<=20 and M==3:
    print("Baliq")
elif D>=21 and M==3 or D<=19 and M==4:
    print("Qo'y")
elif D>=20 and M==4 or D<=20 and M==5:
    print("Buzoq")
elif D>=21 and M==5 or D<=21 and M==6:
    print("Egizaklar")
elif D>=22 and M==6 or D<=22 and M==7:
    print("Qisqichbaqa")
elif D>=23 and M==7 or D<=22 and M==8:
    print("Arslon")
elif D>=23 and M==8 or D<=22 and M==9:
    print("Parizod")
elif D>=23 and M==9 or D<=22 and M==10:
    print("Tarozi")
elif D>=23 and M==10 or D<=22 and M==11:
    print("Chayon")
elif D>=23 and M==11 or D<=21 and M==12:
    print("O'qotar")
elif D>=22 and M==12 or D<=19 and M==1:
    print("Echki")