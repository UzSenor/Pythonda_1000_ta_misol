# 3-misol. Faylning hajmi baytlarda berilgan. Uning hajmini kilobayt va baytlarda ifodalang. 
# 1kb = 1024b
B = int(input("Fayl hajmi (baytda): "))
k = B // 1024
b = B % 1024
print(B, "bayt =", k, "KB", b, "B.")