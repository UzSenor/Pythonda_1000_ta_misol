# Kiritilgan KB ni GB,MB,KB ga aylantirish.
b = int(input("Bayt: "))
bayt = b % 1024
kb = b // 1024 % 1024
mb = b // 1024 // 1024 % 1024
gb = b // 1024 // 1024 // 1024
print(gb, mb, kb, bayt)