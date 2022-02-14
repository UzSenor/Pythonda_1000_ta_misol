#Uyga vazifa hafta kunlari 1-7 bo'lganda
K = int(input("1-365 oraliqdagi kunni kiriting: "))
H_K = int(input("1-7 hafta kunni kiriting: "))
K_K = int(input("Kerak kun: "))
H = ((K_K-K)+H_K+6)%7+1
print(f"Siz kiritgan kuningiz haftaning {H} kuniga to'g'ri keladi")

#Uyga vazifa hafta kunlari 0-6 bo'lganda
K = int(input("1-365 oraliqdagi kunni kiriting: "))
H_K = int(input("1-7 hafta kunni kiriting: "))
K_K = int(input("Kerak kun: "))
H = ((K_K-K)+H_K)%7
print(f"Siz kiritgan kuningiz haftaning {H} kuniga to'g'ri keladi")