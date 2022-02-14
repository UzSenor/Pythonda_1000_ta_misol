# Kun boshidan N sekund o'tganni asr, yil, oy, kun, soat, minut, sekundga aylantirish.
N = int(input("Sekund: "))
S = N % 60
M = N % 3600 // 60 
H = N // 3600 % 24
K = N // 3600 // 24 % 30
O = N // 3600 // 24 // 30 % 360 // 12
Y = N // 3600 // 24 // 30 // 360 % 100
A = N // 3600 // 24 // 30 // 360 // 100
print(f"{N} sekundda - {A} asr {Y} yil {O} oy {K} kun {H} soat {M} minut {S} sekund")