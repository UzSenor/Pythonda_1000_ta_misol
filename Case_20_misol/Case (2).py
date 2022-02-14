# case2. K butun son berilgan. Kiritilgan songa mos baho natijalarini chiqaradigan dastur tuzing.
# 1-yomon, 2-qoniqarsiz, 3-qoniqarli, 4-yaxshi, 5-a'lo. Agar 5 dan katta son kiritilsa xato deb chiqsin
B = int(input("Baho: "))
if B==1:
    B="Yomon"
elif B==2:
    B="Qoniqarsiz"
elif B==3:
    B="Qoniqarli"
elif B==4:
    B="Yaxshi"
elif B==5:
    B="A'lo"
else:
    B="Xato"
print(B)