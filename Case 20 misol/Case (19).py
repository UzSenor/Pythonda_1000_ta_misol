# case19. Sharq kalendarida 60 yillik qabul qilingan. Yil muchali 5 ta rang(yashil, qizil, sariq,
# oq va qora) va 12 ta hayvon(sichqon, sigir, yo'lbars, quyon, ajdar, ilon, ot, qo'y, maymun, tovuq,
# it va to'ng'iz) nomlari kombinatsiyasidan kelib chiqadi. Yilning raqamiga qarab muchalni 
# aniqlaydigan dastur tuzing. 1984-yil boshi "Yashil sichqon yili"
yil = int(input("Yil kiriting(1984-yildan keyingi):"))
farq = yil-1984
rang = farq%5+1
hayvon = farq%12+1
if rang==1:
    rang="Yashil"
elif rang==2:
    rang="Qizil"
elif rang==3:
    rang="Sariq"
elif rang==4:
    rang="Oq"
elif rang==5:
    rang="Qora"
if hayvon==1:
    hayvon="sichqon"
elif hayvon==2:
    hayvon="sigir"
elif hayvon==3:
    hayvon="yo'lbars"
elif hayvon==4:
    hayvon="quyon"
elif hayvon==5:
    hayvon="ajdar"
elif hayvon==6:
    hayvon="ilon"
elif hayvon==7:
    hayvon="ot"
elif hayvon==8:
    hayvon="qo'y"
elif hayvon==9:
    hayvon="maymun"
elif hayvon==10:
    hayvon="tovuq"
elif hayvon==11:
    hayvon="it"
elif hayvon==12:
    hayvon="to'ng'iz"
print(rang, hayvon, "yili")