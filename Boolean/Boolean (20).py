# 20-misol. Uch xonali son berilgan. Jumlani rostlikka tekshiring. Ushbu sonning barch raqamlari 
# har xil.
A = int(input("Uch xonali son: "))
x = A // 100
y = A % 100 // 10
z = A % 10
print(x!=y and y!=z and x!=z)