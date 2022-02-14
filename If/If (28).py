# 28-misol. Yil berilgan (musbat butun son). Berilgan yilda nechta kun borligini aniqlaydigan 
# dastur tuzing. Kabisa yilida 366 kun bor, qolgan yillarda 365 kun bor. Kabisa yili deb 4 ga karrali
# yillarga aytiladi. Lekin 100 ga karrali yillar ichida faqat 400 ga karrali yillar kabisa yili 
# hisoblanadi. Masalan 300, 1300 va 1900 kabisa yili emas. 1200, 2000 yillar kabisa yili
yil = int(input("Yilni kiriting:"))
if yil<100 and yil%4==0 or yil>100 and yil%400==0:
    print("Kabisa yili: 366 kundan iborat")
else:
    print("Yil: 365 kundan iborat")