# 23-misol. Kun boshidan N sekund o'tdi. Kun boshidan boshlab qancha soat, minut va sekund to'liq 
# o'tganini aniqlovchi dastur tuzing.
N = int(input("Kun boshidan o'tgan sekund: "))
M = N // 3600
m = N % 3600 // 60
S = N % 60
print(f"Kun boshidan {M} soat {m} minut {S} sekund o'tdi.")