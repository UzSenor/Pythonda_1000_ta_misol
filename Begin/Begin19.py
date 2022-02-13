# 19-misol. To'g'ri to'rtburchakning qarama-qarshi uchlari kordinatalari berilgan. Uning tomonlari kordinata o'qiga parallel. To'g'ri to'rtburchakning peremetri va yuzini toping.
# a_______________d
# |               |
# |               |¶
# b_______________c
ax = int(input("Ax = ")) #a ning x kordinatasi
ay = int(input("Ay = ")) #a ning y kordinatasi
cx = int(input("Cx = ")) #c ning x kordinatasi
cy = int(input("Cy = ")) #c ning y kordinatasi
bx = ax                  #a ning x kordinatasi b ning x kordinatasiga teng
by = cy                  #c ning y kordinatasi b ning y kordinatasiga teng
dx = cx                  #c ning x kordinatasi d ning x kordinatasiga teng
dy = ay                  #a ning y kordinatasi d ning y kordinatasiga teng
a = abs(ay - by)         # a tomoni uzunligi
b = abs(cx - bx)         # b tomoni uzunligi
P = 2*(a+b)
S = a*b
print("Peremetr: ", P, "\nYuzi: ", S)