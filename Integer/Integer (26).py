# 26-misol. Hafta kunlari quyidagi tartibda berilgan. 1-dushanba, 2-seshanba, 
# 3-chorshanba, 4-payshanba, 5-juma, 6-shanba, 7-yakshanba. 1-365 oraliqqa kiruvchi K soni berilgan.
# Agar 1-yanvar seshanba kuniga to'g'ri kelsa K soni haftaning qaysi kuniga to'g'ri keladi.
Y = int(input("1-365 oraliqdagi kunni kiriting: "))
H = Y % 7 + 1
print(f"Siz kiritgan kuningiz haftaning {H} kuniga to'g'ri keladi")